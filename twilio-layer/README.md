# Create Lambda Layer for Twilio Dependency

1. Create dirs
```PowerShell
mkdir twilio-layer
cd twilio-layer
mkdir python
```

2. Install twilio
```PowerShell
pip install twilio `
  --platform manylinux2014_x86_64 `
  --target python/ `
  --implementation cp `
  --python-version 3.13 `
  --only-binary=:all: --upgrade
```

3. Compress for Upload to Lambda Layer
```PowerShell
Compress-Archive -Path python -DestinationPath twilio-layer-correct.zip
```

Upload zip to Lambda Layer