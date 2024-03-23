# 一些记录

## 打包预先编译的二进制库
```bash
conan export-pkg . name/version@
conan export-pkg . name/version@user/channel
# 2.0 命令如下
conan export-pkg . --name name --version version
conan export-pkg . --name name --version version --user user --channel channel
```

## header only
```bash
conan create . name/version@
conan create . name/version@user/channel
# 2.0 命令如下
conan create . --name name --version version
conan create . --name name --version version --user user --channel channel
```


## revision

Adding `revisions_enabled=1` in the [general] section of your conan.conf file (preferred)

```bash
conan config set general.revisions_enabled=1
```

Setting the `CONAN_REVISIONS_ENABLED=1` environment variable.

```bash
# 在上传的时候也需要设置；这个优先级比上面那个高
export CONAN_REVISIONS_ENABLED=1
```