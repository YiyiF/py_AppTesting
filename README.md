# py_AppTesting

1. 环境依赖
    1. appium 环境配置OK，可正常建立session
      - 方法可参考 [Setting up iOS Real Devices Tests with XCUITest](https://github.com/appium/appium-xcuitest-driver/blob/master/docs/real-device-config.md)

2. 修改 webdriver.py desired_cap中设备相关信息

    - 一个获取 udid & deviceName 的方式
  
    ```
    pip3 install -U tidevice
    tidevice list
    ```
    - 之后会添加自动获取连接的设备信息的方法到webdriver.py中
 
 3. 执行测试用例 py_AppTesting/tests/test_trial.py
 
    RUN Unittests for test_trial.FiltoHomeTests
 
