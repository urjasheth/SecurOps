# SecurOps Approach C: Hybrid Security Tier

Approach C is the **Recommended Enterprise Standard** for developers who need high-fidelity security without the disk overhead of Docker. It combines the advanced verification of Approach A with the native speed of Approach B.

## 🚀 One-Command Setup

Run the following command in your project root to install and configure all security tools:

```bash
bash securops-config-approch-c/scripts/setup-hybrid.sh
```

## 🔗 CI/CD Integration

Approach C includes a pre-configured GitHub Actions workflow:
- **Location**: `.github/workflows/securops-hybrid.yml`
- **Scans**: Automatically runs TruffleHog (Verified), Semgrep (Hybrid), and Trivy on every push and pull request.
- **Setup**: The setup script automatically copies this to your project's `.github` directory.

## 📊 Comparative Strategy Matrix

| Feature | Approach B (Standard) | Approach A (Advanced) | **Approach C (Hybrid)** |
| :--- | :--- | :--- | :--- |
| **System Requirement** | Native | **Docker (High Disk)** | **Native (Low Disk)** |
| **Secret Detection** | Pattern Matching | API Verification (Pings) | **API Verification (Pings)** |
| **SAST Rules** | Generic | Mobile Specific | **Mobile, .NET, & PHP** |
| **Speed** | Fast | Slow (Container Start) | **Very Fast** |
| **Fidelity** | Medium | High | **High** |

## 🛡️ Technology Support

Approach C is configured to scan all organizational technology stacks in a single pass:
- **Mobile**: Android (Java/Kotlin), iOS (Swift), Flutter (Dart).
- **Web**: JavaScript, HTML/CSS.
- **Enterprise**: .NET (C#), PHP.

## 🛠️ Requirements
- **pre-commit** (`pip install pre-commit`)
- **TruffleHog** (Native binary)
- **Semgrep** (`pip install semgrep`)
- **Trivy** (Native binary)

*Note: If local binaries are missing, the setup script will provide download links or installation commands.*
