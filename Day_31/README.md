# Secure File Upload API

A secure, high-performance file upload REST API built with **Python** and **FastAPI**. This project addresses critical security vulnerabilities commonly associated with web uploads, including path traversal, arbitrary code execution, MIME-spoofing, and Denial of Service (DoS).

---

## Features & Security Measures

- **Client Filename Sanitization**: Utilizes `werkzeug.utils.secure_filename` to neutralize relative path directory traversal attacks (`../../`).
- **Cryptographic Storage Names**: Uploaded files are renamed using `UUIDv4` hex strings to prevent overwrites, file enumeration, and sensitive data leakage.
- **Deep Content Inspection (Magic Bytes)**: Validates actual binary signatures via `libmagic` instead of relying on spoofable client headers (`Content-Type`) or extensions alone.
- **Streaming Size Enforcement**: Upload streams are inspected and counted in 1 MB chunks to abort downloads exceeding size thresholds immediately, mitigating server memory exhaustion (DoS)[cite: 1].
- **Storage Isolation**: Saves files outside the source code tree in a dedicated folder[cite: 1].
- **Automatic Cleanup**: Partial files created during failed or aborted uploads are unlinked and destroyed immediately.

---

## Project Structure

```text
secure-file-upload-api/
├── safe_storage/            # Target storage location for validated files
├── main.py                  # API endpoints, validation logic, and error handlers
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
