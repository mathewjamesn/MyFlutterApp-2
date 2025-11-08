# My Flutter App

A Flutter mobile application with menu items that display toast messages.

## Features

- Two menu buttons: "Menu 1" and "Menu 2"
- Toast messages displayed when each menu item is clicked
- Clean and simple Material Design UI

## Getting Started

### Prerequisites

- Flutter SDK (3.0.0 or higher) - [Installation Guide](https://docs.flutter.dev/get-started/install)
- Dart SDK
- Android Studio / VS Code with Flutter extensions
- Android SDK for building APK

**Note:** Make sure Flutter is added to your system PATH after installation.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mathewjamesn/MyFlutterApp-2.git
cd MyFlutterApp-2
```

2. Install dependencies:
```bash
flutter pub get
```

3. Run the app:
```bash
flutter run
```

### App Icon Setup

The app uses Android vector drawable icons (XML-based). If you want to use custom PNG icons:

1. Place your 1024x1024 icon at `assets/icon/app_icon.png`
2. Add `flutter_launcher_icons` to `pubspec.yaml`:
```yaml
dev_dependencies:
  flutter_launcher_icons: ^0.13.1

flutter_launcher_icons:
  android: true
  image_path: "assets/icon/app_icon.png"
```
3. Run: `flutter pub run flutter_launcher_icons`

Alternatively, a Python script (`generate_icon.py`) is included to create a simple icon:
```bash
pip install Pillow
python generate_icon.py
```

### Building APK

To build a release APK manually:
```bash
flutter build apk --release
```

The APK will be generated at: `build/app/outputs/flutter-apk/app-release.apk`

## GitHub Actions

This project includes a GitHub Actions workflow that automatically builds the APK when you push to the main/master branch.

### Setup

1. Push this code to your GitHub repository
2. The workflow will automatically trigger on:
   - Push to main/master branch
   - Pull requests to main/master branch
   - Manual workflow dispatch

3. After the build completes:
   - The APK will be available as an artifact in the Actions tab
   - A release will be created automatically with the APK attached (on push to main/master)

### Workflow Features

- ✅ Automated APK building
- ✅ APK artifact upload
- ✅ Automatic release creation with version tagging
- ✅ Java 17 and Flutter 3.24.0 configured

## Project Structure

```
MyFlutterApp-2/
├── .github/
│   └── workflows/
│       └── build.yml          # GitHub Actions workflow
├── android/                    # Android-specific files
├── lib/
│   └── main.dart              # Main application code
├── pubspec.yaml               # Project dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Dependencies

- `flutter`: Flutter SDK
- `fluttertoast`: ^8.2.4 - For displaying toast messages

## License

This project is open source and available under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
