<template>
  <div class="Aside">
    <el-col>
      <el-menu
        style="font-size: 30px"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        background-color="#008C8C"
        text-color="#fff"
        active-text-color="#ffd04b"
        default-openeds="[1,2]"
        router
      >
        <el-submenu index="1">
          <template slot="title">
            <i
              class="el-icon-user-solid"
              style="font-size: 20px; color: #fff"
            ></i>
            <span>个人信息</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/person/info">信息查看</el-menu-item>
            <el-menu-item index="/person/score">成绩查询</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-s-order" style="font-size: 20px; color: #fff"></i>
            <span>课程选择</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/person/change">课程计划</el-menu-item>
            <el-menu-item index="/course/choose">选课</el-menu-item>
            <el-menu-item index="/course/close">退课</el-menu-item>
            <el-menu-item index="/course/check">已选课程</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <!-- <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">课程选择</span>
        </el-menu-item> -->
        <!-- <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">课程选择</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <i class="el-icon-document"></i>
          <span slot="title">导航三</span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-setting"></i>
          <span slot="title">导航四</span>
        </el-menu-item> -->
      </el-menu>
    </el-col>
  </div>
</template>


<script>
export default {
  name: "Aside",
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>


<style lang="sass">
.el-submenu__title
  font-size: 20px
.el-menu-item
  font-size: 16px
</style>