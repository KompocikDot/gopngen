# GOPNGEN

## Usage:
 - Make an windows image with `UAC` disabled (important to skip some user authorization) 
 - Rename `.settings.example` to `.settings`
 - Fill the values inside it and do not forget to add permissions to use ec2 for aws user
 - run `go main.go` or build app and run `./main`

#### Technologies used:
 - golang
   - go-aws-sdk/v2

 - python
   - playwright (may switch to pure `requests` later)
   - pyautogui + opencv

 - docker (soon)
