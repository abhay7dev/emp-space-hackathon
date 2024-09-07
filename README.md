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
py -m venv env
./env/Scripts/activate

./env/Scripts/pip3 install openai
./env/Scripts/pip3 install python-dotenv

cd ..

cd web
npm i
npm run start
```