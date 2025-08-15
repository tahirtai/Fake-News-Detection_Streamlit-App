# 🌟 ExplorerBlurMica - Update Log (English Version)

This software is **free and open-source**, licensed under **LGPLv3**  
GitHub: https://github.com/Maplespe/ExplorerBlurMica

---

##  Version 2.0.1 (2024-02-12)

- Compatible with Windows 11 Preview Canary 23H2 26040 and 24H2 26052.
- Optimized compatibility with StartAllBack.
- Fixed the opaque color of the title bar when opening it for the first time after reboot using the Mica effect.
- Added `MicaAlt` effect option. Use `effect=4` to enable. Now `effect=2` is for the normal Mica effect.
- Restored `showLine` option. You can now hide the split line between TreeView and DUI view with `showLine=true`.

 Updated and optimized registration and uninstall scripts.  
 Thanks to: `OnCloud125252`

---

##  Version 2.0.0 (2024-01-01)

> This version is a complete refactor from scratch, focusing on **stability** and **performance**.

### New Config Options:
- `clearWinUIBg`: Removes WinUI and Xaml toolbar backgrounds in Windows 11.

### Config File Changes:
- Removed: `[smallBorder]`, `[showLine]`, `[darkRibbon]`

### Bug Fixes:
- Fixed Ribbon rendering issues on Windows 10 — removed `[darkRibbon]` option as it's no longer needed.
- Fixed compatibility with Windows 11 23H2, Dev, Canary builds — supports new File Explorer using WinUI.
- Fixed rendering issues for most Control Panel components (some legacy components are too hard to maintain).
- Fixed Preview Panel text rendering and added support for WinUI version.
- Fixed scrollbar color issues in address bar dropdown when using `clearBarBg`.
- Fixed rendering of BingSearchSuggestionsBox on Windows 10.
- Switched from BHO to FolderExtension COM component for loading (performance and compatibility boost).
- Improved compatibility with StartAllBack and various third-party software.
- Optimized TreeView and DUI split line — made consistent with toolbar line and removed `[showLine]` option.
- Fixed Acrylic blur boundary issue in Windows 10 — removed `[smallBorder]` option since fix is now default.
- General performance and stability optimizations (additional updates on 2024-01-03).

### Other:
From this version onward, full source code (*.cpp) is no longer released, only partial header files (*.h).  
This is due to violations of the open-source license by some users.  
Those who understand the principles will still be able to comprehend the implementation from the headers alone, rather than rebranding this project as paid software.

---

## 📦 Version 1.0.7 (2023-08-11)

### New Config Options:
- `clearAddress`: Clears the background color of the address bar.  
  > ⚠️ If using StartAllBack, disable "Classic search box on the right" or it will override this feature.
- `clearBarBg`: Clears scrollbar background color.  
  > ⚠️ Scrollbars are custom-drawn and may not match system style.
- `effect=3`: Enables Blur (Clear) effect — pure blur without color.

### Config Changes:
- Replaced `[blend]` with `[light]` and `[dark]` for better color adaptation.

### Bug Fixes:
- Fixed "showLine" not working on old tabs when new tabs are opened in multi-tab Explorer.
- Fixed window effect loss when changing DPI or switching displays.
- Fixed rendering of Properties page and File Dialog in File Explorer.
- Other rendering optimizations.

---

## 📦 Version 1.0.6 (2023-05-01)

### New Config Options:
- `showLine`: Toggle separator line between TreeView and Preview Panel.
- `darkRibbon`: Forces Ribbon to dark mode in Windows 10 Light theme to fix incorrect text/background rendering.

### Fixes:
- Fixed Acrylic blur effect exceeding window borders in Windows 10.  
  `smallBorder` now defaults to `false`.

---

## 📦 Version 1.0.5 (2023-04-29)

- Fixed compatibility issues with navigation bar tweaks using StartAllBack and similar software.
- Fixed rendering problems in Control Panel and certain shell-opened pages.
- Improved performance and code efficiency.

---

## 📦 Version 1.0.4 (2023-01-12)

- Fixed potential background rendering errors in specific conditions.
- Fixed rendering of Control Panel command module and navigation bar.
- Fixed text color rendering error with Microsoft IME input method.

---

## 📦 Version 1.0.3 (2022-11-21)

- Fixed opaque address bar in Windows 10 dark theme.
- Fixed incorrect Blur and Acrylic effect ID mappings in config for Windows 10.

---

## 📦 Version 1.0.2 (2022-10-22)

- Added support for Windows 22H2 and multi-tab Explorer.
- Fixed white vertical bar on the far left of Windows 11.
- Fixed opaque address bar in Windows 11 dark mode.
- Improved program stability.
- Added Acrylic support for Windows 11.  
  `effect=2` now enables Mica.

---

## 📦 Version 1.0.1 (2022-08-27)

- Fixed opaque Ribbon bar issue in Windows 10 English language system.

---

