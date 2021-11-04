<template>
  <div class="Nav">
    <div class="name">课程选择系统</div>
    <div class="status">{{ username }}，欢迎您进入课程选择系统</div>
    <div class="check">
      <el-button @click="login" style="font-size: 20px" type="primary"
        >注销</el-button
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "Nav",
  data() {
    var username = "";
    // alert("o我测试一下");
    if (window.localStorage.getItem("is_student") == "true") {
      this.$axios
        .get("stu/getStuInfo/userid=" + window.localStorage.getItem("userid"))
        .then((res) => {
          this.username = res.data.data[0].name;
          // alert(this.username);
        });
    } else {
      username = "管理员老师";
    }
    return {
      username,
    };
  },
  methods: {
    login() {
      // 先跳转到登录页
      this.$router.push("/login");
      this.$message({
        message: "注销成功！",
        type: "success",
      });
      window.localStorage.clear();
    },
  },
};
</script>

<style  scoped>
.Nav {
  display: flex;
  justify-content: space-between;
}
.name {
  font-size: 30px;
  font-weight: bold;
  color: #fff;
  -webkit-text-stroke: 1px #969696;
}
.status {
  font-size: 20px;
  font-weight: bold;
  color: #fff;
  -webkit-text-stroke: 0.5px #969696;
}
</style>
