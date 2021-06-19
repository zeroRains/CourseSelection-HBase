<template>
  <div class="DelCourseSchedule">
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
      <el-table-column label="课程序号" prop="cno"> </el-table-column>
      <el-table-column label="课程代码" prop="coursecode"> </el-table-column>
      <el-table-column label="课程名称" prop="cname"> </el-table-column>
      <el-table-column label="开始周" prop="startweek"> </el-table-column>
      <el-table-column label="结束周" prop="endweek"> </el-table-column>
      <el-table-column label="星期" prop="day"> </el-table-column>
      <el-table-column label="节次" prop="index"> </el-table-column>
      <el-table-column label="学分" prop="credit"> </el-table-column>
      <el-table-column label="教室" prop="classroom"> </el-table-column>
      <el-table-column label="可选人数" prop="optional"> </el-table-column>
      <el-table-column label="已选人数" prop="selected"> </el-table-column>
      <el-table-column align="right">
        <template slot="header">
          <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
        </template>
        <template slot-scope="test">
          <el-button type="danger" @click="handleEdit(test.$index, test.row)"
            >删除计划</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "DelCourseSchedule",
  data() {
    var tableData;
    this.$axios
      .get(
        "teacher/getCourseScheduleTable/userid=" +
          window.localStorage.getItem("userid")
      )
      .then((res) => {
        this.tableData = res.data.data;
      });
    return {
      tableData,
    };
  },
  methods: {
    handleEdit(index, row) {
      this.$axios
        .get("teacher/delCourseScheduleTable/cno=" + row.cno)
        .then((res) => {
          console.log(res);
          if (res.data.status == "success") {
            this.$message({
              message: "删除成功!",
              type: "success",
            });
            location.reload();
          } else {
            this.$message.error("删除失败！");
          }
        });
      // alert(row.cno);
      console.log(index, row);
    },
  },
};
</script>