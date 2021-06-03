<template>
  <div id="app">
    <el-container>
      <el-header><Nav /></el-header>
      <el-container>
        <el-aside width="200px">这里放索引</el-aside>
        <el-main>这里是主要显示区</el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
import Nav from "./components/Nav";

export default defineComponent({
  components: {
    Nav,
  },
  setup() {},
});
</script>


<style lang="scss">
.el-header,
.el-footer {
  background-color: #b3c0d1;
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
