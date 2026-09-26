import json
import logging
import sys
import pandas as pd


def setup_logger(log_file: str) -> logging.Logger:
    """Configures structured file and console logging."""
    logger = logging.getLogger("ETLPipeline")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler
    fh = logging.FileHandler(log_file, mode="w")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


class ETLPipeline:

    def __init__(self, config_path: str):
        with open(config_path, "r") as f:
            self.config = json.load(f)

        log_path = self.config.get("logging", {}).get(
            "log_file", "pipeline.log"
        )
        self.logger = setup_logger(log_path)
        self.logger.info("Pipeline configuration loaded successfully.")

    def extract(self) -> pd.DataFrame:
        """Reads input data from the configured source."""
        source_path = self.config["extract"]["source_file"]
        self.logger.info(f"Starting EXTRACT phase from: {source_path}")

        df = pd.read_csv(source_path)
        self.logger.info(f"Extracted {len(df)} records.")
        return df

    def validate(self, df: pd.DataFrame) -> pd.DataFrame:
        """Validates schema integrity and null thresholds."""
        val_cfg = self.config.get("validate", {})
        self.logger.info("Starting VALIDATION phase.")

        # Check required columns
        for col in val_cfg.get("required_columns", []):
            if col not in df.columns:
                err_msg = f"Validation Failed: Missing required column '{col}'"
                self.logger.error(err_msg)
                raise ValueError(err_msg)

        # Drop records failing non-null requirements
        for col in val_cfg.get("non_null_columns", []):
            null_count = df[col].isnull().sum()
            if null_count > 0:
                self.logger.warning(
                    f"Found {null_count} nulls in '{col}'. Dropping invalid records."
                )
                df = df.dropna(subset=[col])

        self.logger.info(
            f"Validation complete. Valid records remaining: {len(df)}"
        )
        return df

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Applies configured transformations sequentially."""
        self.logger.info("Starting TRANSFORM phase.")
        transformations = self.config.get("transform", [])

        for step in transformations:
            t_type = step.get("type")

            if t_type == "clean_strings":
                for col in step.get("columns", []):
                    if col in df.columns:
                        df[col] = df[col].astype(str).str.strip()
                self.logger.info(
                    f"Trimmed whitespace on columns: {step.get('columns')}"
                )

            elif t_type == "filter_numeric_range":
                col = step["column"]
                min_v = step.get("min_value", float("-inf"))
                max_v = step.get("max_value", float("inf"))
                initial_count = len(df)
                df = df[(df[col] >= min_v) & (df[col] <= max_v)]
                dropped = initial_count - len(df)
                self.logger.info(
                    f"Filtered '{col}' between [{min_v}, {max_v}]. Dropped {dropped} records."
                )

            elif t_type == "add_column":
                new_col = step["new_column"]
                expr = step["expression"]
                df = df.eval(f"{new_col} = {expr}")
                self.logger.info(
                    f"Added calculated column '{new_col}' via expression: {expr}"
                )

        self.logger.info(
            f"Transformation complete. Output record count: {len(df)}"
        )
        return df

    def load(self, df: pd.DataFrame) -> None:
        """Writes transformed dataset to the configured destination."""
        out_cfg = self.config["load"]
        target_path = out_cfg["output_file"]
        self.logger.info(f"Starting LOAD phase to destination: {target_path}")

        if out_cfg.get("format") == "csv":
            df.to_csv(target_path, index=False)

        self.logger.info(
            f"Successfully saved {len(df)} records to {target_path}."
        )

    def run(self):
        """Executes the full pipeline flow."""
        self.logger.info("ETL Pipeline job triggered.")
        try:
            raw_data = self.extract()
            validated_data = self.validate(raw_data)
            final_data = self.transform(validated_data)
            self.load(final_data)
            self.logger.info("ETL Pipeline finished successfully.")
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {str(e)}")
            raise


if __name__ == "__main__":
    pipeline = ETLPipeline("pipeline_config.json")
    pipeline.run()
