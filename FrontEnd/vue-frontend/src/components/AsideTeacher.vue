<template>
  <div class="AsideTeacher" style="height: 100%">
    <el-col style="height: 100%">
      <el-menu
        style="font-size: 30px; height: 100%"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        background-color="#008C8C"
        text-color="#fff"
        active-text-color="#ffd04b"
        default-openeds="[1,2,3]"
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
            <el-menu-item index="/teacher/info">信息查看</el-menu-item>
            <!-- <el-menu-item index="/teacher/change">修改信息</el-menu-item> -->
          </el-menu-item-group>
        </el-submenu>
        <!-- <el-menu-item index="/teacher/score">
          <i
            class="el-icon-edit-outline"
            style="font-size: 20px; color: #fff"
          ></i>
          <span slot="title" style="font-size: 20px">成绩管理</span>
        </el-menu-item> -->
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-s-order" style="font-size: 20px; color: #fff"></i>
            <span>课程管理</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/teacher/courseschedule"
              >课程计划</el-menu-item
            >
            <el-menu-item index="/teacher/delcourseschedule"
              >删除课程计划</el-menu-item
            >
            <el-menu-item index="/teacher/course">我的课程</el-menu-item>
            <!-- <el-menu-item index="/teacher/delcourse">删除课程</el-menu-item> -->
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-col>
  </div>
</template>


<script>
export default {
  name: "AsideTeacher",
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