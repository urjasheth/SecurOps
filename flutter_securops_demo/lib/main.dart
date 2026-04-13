import 'dart:math';
import 'package:flutter/material.dart';

// ❌ Critical: Hardcoded Internal API Key!
// Semgrep will catch this as a blocking error.
const String companyApiKey = "XoR-12345-securops-demo-key-verified";

// ❌ Warning: Hardcoded internal endpoint!
// Semgrep rules will catch this as a blocking error.
const String internalEndpoint = "https://api.staging.internal.company.com/v1/auth";

// ❌ Critical: Hardcoded Secret Key!
// Semgrep will catch this as a blocking error.
var secret_key = "DEMO-SECRET-12345678-FAIL";

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text("SecurOps Demo")),
        body: Center(
          child: ElevatedButton(
            onPressed: () {
              // ❌ Warning: Standard Random used!
              // Semgrep will catch this insecure random.
              var randomValue = Random().nextInt(100);
              print("Lucky number: $randomValue");
            },
            child: const Text("Generate Insecure Random"),
          ),
        ),
      ),
    );
  }
}
