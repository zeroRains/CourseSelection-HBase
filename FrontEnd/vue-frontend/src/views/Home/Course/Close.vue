<template>
  <div class="Close">
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

      <el-table-column align="center">
        <template slot="header">
          <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
        </template>
        <template slot-scope="test">
          <el-button type="danger" @click="handleEdit(test.$index, test.row)"
            >退课</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "Close",
  data() {
    var tableData;
    this.$axios
      .get(
        "/stu/deleteCourseList/userid=" + window.localStorage.getItem("userid")
      )
      .then((res) => {
        this.tableData = res.data.data;
      });
    return {
      search: "",
      tableData,
    };
  },
  methods: {
    handleEdit(index, row) {
      this.$axios
        .post(
          "stu/delStuCourse/userid=" +
            window.localStorage.getItem("userid") +
            "&cno=" +
            row.coursecode
        )
        .then((res) => {
          if (res.data.status == "success") {
            location.reload();

            this.$message({
              message: "退课成功！",
              type: "success",
            });
          } else {
            this.$message.error("退课失败！");
          }
        });
    },
  },
};
</script>