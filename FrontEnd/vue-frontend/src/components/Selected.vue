<template>
  <div class="Selected">
    <el-button type="primary" @click="getPostion">选课</el-button>
  </div>
</template>
<script>
export default {
  name: "Selected",
  props: {
    position: [],
  },
  data() {
    var tableData;

    return {
      dialogTableVisible: false,
      tableData,
    };
  },
  methods: {
    handleEdit(index, row) {
      this.$axios
        .post(
          "/stu/selectCourse/userid=" +
            window.localStorage.getItem("userid") +
            "&cno=" +
            row.cno
        )
        .then((res) => {
          if (res.data.status == "success") {
            this.$message({
              message: "选课成功！",
              type: "success",
            });
            this.dialogTableVisible = false;
            location.reload();
          } else {
            this.$message.error("课程冲突，选择失败！");
          }
        });
    },
    getPostion() {
      this.$axios
        .get("stu/isChoosible/coursecode=" + this.position)
        .then((res) => {
          var temp = res.data.data;

          if (temp.length != 0) {
            this.tableData = temp;
            this.dialogTableVisible = true;
          } else {
            this.$message.error("当前课程没有可选的课号！");
          }
        });
      alert(this.position);
    },
  },
};
</script>

<style>
.customWidth {
  width: 90%;
  height: 70%;
}
</style>