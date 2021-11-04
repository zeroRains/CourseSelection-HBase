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
        default-openeds="[1]"
        router
      >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-s-order" style="font-size: 20px; color: #fff"></i>
            <span>信息导入</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/teacher/courseschedule"
              >导入学生信息</el-menu-item
            >
            <el-menu-item index="/teacher/delcourseschedule"
              >导入课程信息</el-menu-item
            >
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