<template>
  <div class="Nav">
    <div class="name">课程选择系统</div>
    <div class="status" v-if="is_login">
      {{ username }}，欢迎您进入课程选择系统
    </div>
    <div class="status" v-else>您还未登录，请先登录哦</div>
    <div class="check" v-if="is_login">
      <el-button @click="logout" style="font-size: 20px" type="primary"
        >注销</el-button
      >
    </div>
    <div class="check" v-else>
      <el-button @click="login" style="font-size: 20px" type="primary"
        >登录</el-button
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "Nav",
  data: () => {
    return {
      is_login: true,
      username: "小明",
    };
  },
  methods: {
    logout() {
      this.is_login = false;
    },
    login() {
      // 这里要先跳转到登录页，然后进行登录
      // 确认登录成功后才进行修改
      this.is_login = true;
      // 同时还要修改用户的名称
      this.username = "小王";
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
}
</style>
