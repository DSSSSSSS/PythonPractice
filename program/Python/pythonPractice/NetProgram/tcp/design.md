# design

## login

认证、授权、会话建立、取消会话

1. 登录时进行格式正则验证，减少不必要的数据库访问。
2. 密码保存应使用hash。
3. 通过比对cookie和seesion信息来验证用户是否登录。
4. 在cookie中添加token、登录序列。

### SSO(Single Sign On) 单点登录问题

