<template>
  <div class="Choose">
    <el-table
      :header-row-style="{ lineHeight: '30px' }"
      :data="
        tableData.filter(
          (data) =>
            !search || data.name.toLowerCase().includes(search.toLowerCase())
        )
      "
      style="width: 100%"
    >
      <el-table-column align="center" label="课号" prop="coursecode">
      </el-table-column>
      <el-table-column align="center" label="课程名称" prop="name">
      </el-table-column>
      <el-table-column align="center" label="学分" prop="credit">
      </el-table-column>
      <el-table-column align="center" label="学年" prop="time">
      </el-table-column>
      <el-table-column align="center" label="老师" prop="teacher">
      </el-table-column>
      <el-table-column align="right">
        <template slot="header">
          <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
        </template>
        <template slot-scope="test">
          <div
            style="width: 40px; height: 40px"
            @mousedown="handleEdit(test.$index, test.row)"
          >
            <el-button type="primary">选课</el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "Choose",

  data() {
    var tableData = [];
    // close.log(tableData);
    this.$axios
      .get("stu/selectCourse/userid=" + window.localStorage.getItem("userid"))
      .then((res) => {
        var temp = res.data.data;
        // console.log(temp);
        for (let a of temp) {
          // console.log(a.coursecode);
          this.tableData.push({
            coursecode: a.coursecode,
            name: a.name,
            credit: a.credit,
            time: a.time,
            teacher: a.teacher,
            visible: true,
          });
        }
      });
    return {
      tableData,
      search: "",
      position: "123",
    };
  },
  methods: {
    handleEdit(index, row) {
      // alert("游泳");
      this.$axios
        .get(
          `stu/addStuCourse/userid=${window.localStorage.getItem(
            "userid"
          )}&cno=${row.coursecode}`
        )
        .then((res) => {
          if (res.data.status == "success") {
            // location.reload();
            row.visible = false;
            this.$message({
              message: "选课成功！",
              type: "success",
            });
          } else {
            this.$message.error("选课失败！");
          }
        });
    },
  },
};
</script>
<style lang="scss" scoped>
.el-table__header {
  height: 40px;
}
</style>