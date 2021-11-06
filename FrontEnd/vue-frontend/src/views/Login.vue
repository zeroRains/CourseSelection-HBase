<template>
  <div class="Login">
    <div>
      Made by 1900301236谢浚霖、1900300819卢林军
      <br>
    </div>
    <div class="main">
      <div class="temp">
        <div style="border-bottom: 1px solid">
          <i class="el-icon-user-solid"></i>
          用户登录
        </div>
        <div
          style="
            margin-top: 20px;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
          "
        >
          课程选择系统
        </div>
        <div
          style="
            width: 350px;
            position: absolute;
            left: 0;
            right: 0;
            margin: 0 auto;
          "
        >
          <el-form
            :model="ruleForm"
            :rules="rules"
            ref="ruleForm"
            class="demo-ruleForm"
            hide-required-asterisk="false"
          >
            <!-- prop是要校验的类型,尽量让校验的方式和后端字段一致 -->
            <el-form-item label="用户名" prop="user">
              <el-input v-model="ruleForm.user"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input type="password" v-model="ruleForm.password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-radio-group v-model="ruleForm.resource" size="medium">
                <el-radio border label="学生端"></el-radio>
                <el-radio border label="教师端"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" style="font-size: 20px" @click="login()"
                >登录</el-button
              >
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      ruleForm: {
        user: "1900300101",
        password: "123456",
        resource: "学生端",
      },
      rules: {
        user: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          {
            min: 5,
            max: 10,
            message: "长度在 5 到 10 个字符",
            trigger: "blur",
          },
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            min: 6,
            max: 16,
            message: "长度在 3 到 16 个字符",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    login() {
      if (this.ruleForm.resource == "学生端") {
        this.$axios
          .post(
            "/stu/stuLogin/sno=" +
              this.ruleForm.user +
              "&passwd=" +
              this.ruleForm.password
          )
          .then((res) => {
            if (res.data.status == "success") {
              window.localStorage.setItem("userid", res.data.data);
              window.localStorage.setItem("is_student", "true");
              this.$message({
                message: "登录成功！欢迎使用课程选择系统！",
                type: "success",
              });
              this.$router.push("/");
            } else {
              this.$message.error("帐号或者密码或者身份错误!");
            }
          });
      } else {
        if (
          this.ruleForm.user == "admin" &&
          this.ruleForm.password == "123456"
        ) {
          window.localStorage.setItem(
            "userid",
            "1d892a74-d740-3198-9c1f-db4f132ff577"
          );
          window.localStorage.setItem("is_student", "false");
          this.$message({
            message: "登录成功！欢迎使用课程选择系统！",
            type: "success",
          });
          this.$router.push("/");
        } else {
          this.$message.error("帐号或者密码或者身份错误!");
        }
      }
    },
  },
};
</script>


<style lang="sass">
*
  margin: 0
  padding: 0
  .main
    width: 100%
    height: 100%
    position: absolute
    background-color: #e2e4e3
    .temp
      -webkit-box-shadow: #666 0px 0px 10px
      width: 700px
      height: 450px
      position: fixed
      left: 0
      right: 0
      top: 0
      bottom: 0
      margin: auto
</style>
