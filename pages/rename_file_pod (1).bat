@echo off
setlocal EnableDelayedExpansion

echo.
set /p "PDF_FOLDER=Masukkan path folder tempat file PDF berada (contoh: D:\Data\TripPDFs): "

if not exist "%PDF_FOLDER%" (
    echo.
    echo Folder tidak ditemukan. Pastikan path sudah benar dan coba lagi.
    pause
    exit /b
)

REM Cek apakah Python tersedia
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo Python tidak ditemukan. Mengunduh dan menginstal...

    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -OutFile python_installer.exe"
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
    echo Python berhasil diinstal.
) else (
    echo Python sudah terinstal.
)

REM Tulis script Python
echo import os> rename_script.py
echo folder_path = r"%PDF_FOLDER%">> rename_script.py
echo for filename in os.listdir(folder_path):>> rename_script.py
echo     if filename.endswith(".pdf"):>> rename_script.py
echo         parts = filename.split("_")>> rename_script.py
echo         if len(parts) ^>= 3:>> rename_script.py
echo             new_name = parts[1] + ".pdf">> rename_script.py
echo             old_path = os.path.join(folder_path, filename)>> rename_script.py
echo             new_path = os.path.join(folder_path, new_name)>> rename_script.py
echo             os.rename(old_path, new_path)>> rename_script.py
echo             print("Renamed:", filename, "->", new_name)>> rename_script.py

echo.
echo Menjalankan proses rename...
python rename_script.py

REM Hapus script Python
if exist "rename_script.py" del /f /q "rename_script.py"

echo.
echo Selesai! File sudah di-rename di folder: %PDF_FOLDER%
pause