
[app]

title = MY AI 3.0

package.name = myai3
package.domain = org.mohammed

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,pdf

version = 3.0

requirements = python3,kivy,requests,plyer,pypdf,pyjnius

orientation = all

fullscreen = 0

# Android configuration
android.api = 35
android.minapi = 23
android.archs = arm64-v8a

android.permissions = INTERNET,RECORD_AUDIO,READ_EXTERNAL_STORAGE

android.private_storage = True

android.allow_backup = False

android.enable_androidx = True

p4a.bootstrap = sdl2

[buildozer]

log_level = 2

warn_on_root = 1
