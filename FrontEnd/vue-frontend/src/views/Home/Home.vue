<template>
  <div class="home">
    <el-container>
      <el-header><Nav /></el-header>
      <el-container>
        <el-aside width="200px"><Aside /></el-aside>
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
export default {
  name: "Home",
  components: {
    Nav,
    Aside,
  },
};
</script>
<style lang="scss">
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
