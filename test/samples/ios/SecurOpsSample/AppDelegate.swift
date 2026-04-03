import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    // Hardcoded API key for Gitleaks/Semgrep to detect
    let apiKey = "AIzaSyAB-CD1234567890EFGHIJKLMnopqrstuvw"

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Insecure HTTP request pattern
        let url = URL(string: "http://insecure.example.com")!
        print("Insecure URL: \(url)")
        return true
    }
}
