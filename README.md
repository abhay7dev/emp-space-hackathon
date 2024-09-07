# TerraTest

## Building and Running

Running from powershell:
```pwsh
cd backend-python
py -m venv env
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
./env/Scripts/activate.ps1

./env/Scripts/pip3.exe install openai
./env/Scripts/pip3.exe install python-dotenv

cd ..

cd web
npm i
npm run start
```

Running from POSIX-Compliant shell
```bash
cd backend-python
python -m venv env
chmod +x ./env/bin/activate ./env/bin/pip
./env/bin/activate

./env/bin/pip install openai python-dotenv

cd ..

cd web
npm i
npm run start
```