<template>
  <div class="Check">
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
      <el-table-column align="center" label="成绩" prop="score">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "Check",
  data() {
    var tableData;
    this.$axios
      .get(
        "stu/getStuScore/userid=" + window.localStorage.getItem("userid")
      )
      .then((res) => {
        this.tableData = res.data.data;
        // alert(this.tableData.status);
      });
    return {
      tableData,
    };
  },
};
</script>