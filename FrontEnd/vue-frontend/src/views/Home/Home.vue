<template>
  <div class="home" style="height: 100%">
    <el-container style="height: 100%">
      <el-header><Nav /></el-header>
      <el-container style="height: 100%">
        <el-aside width="200px" style="height: 100%"
          ><Aside v-if="is_student" />
          <AsideTeacher v-else />
        </el-aside>

        <!-- <el-aside width="200px"><Aside /></el-aside> -->

        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from "@/components/Nav";
import Aside from "@/components/Aside";

import AsideTeacher from "@/components/AsideTeacher";

export default {
  name: "Home",
  components: {
    Nav,
    AsideTeacher,
    Aside,
  },
  data: () => {
    // window.localStorage.setItem("is_student", false);
    return {
      is_student:
        window.localStorage.getItem("is_student") == "true" ? true : false,
    };
  },
  beforeCreate() {
    if (window.localStorage.getItem("userid") == null) {
      this.$message.error("您还未登录，请您先登录！");
      this.$router.push("/login");
    }
  },
};
</script>
<style lang="scss">
* {
  margin: 0;
  padding: 0;
}
.el-header,
.el-footer {
  background-color: #009e9e;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}
body > .el-container {
  margin-bottom: 40px;
}
.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}
.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
