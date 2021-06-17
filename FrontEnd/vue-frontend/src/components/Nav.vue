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
    return {
      username: "",
    };
  },
  mounted() {
    this.$axios
      .post("/getStuInfo/6fe4ad65-f590-390a-a6a1-123c022b01eb")
      .then((res) => {
        console.log(res);
      });
  },
  methods: {
    login() {
      // 先跳转到登录页
      this.$router.push("/login");
      // 这里要先跳转到登录页，然后进行登录

      // 同时还要修改用户的名称
      this.username = "";
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
