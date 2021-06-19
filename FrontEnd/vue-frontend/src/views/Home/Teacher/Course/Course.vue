<template>
  <div class="Courese">
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
      <el-table-column align="center" label="课程序号" prop="cno">
      </el-table-column>
      <el-table-column align="center" label="课程名称" prop="credit">
      </el-table-column>
      <el-table-column align="center" label="学分" prop="cname">
      </el-table-column>
      <el-table-column align="center" label="可选人数" prop="optional">
      </el-table-column>
      <el-table-column align="center" label="已选人数" prop="selected">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "Courese",
  data() {
    var tableData;
    this.$axios
      .get(
        "teacher/getTeachTable/userid=" + window.localStorage.getItem("userid")
      )
      .then((res) => {
        this.tableData = res.data.data;
      });

    return {
      tableData,
    };
  },
};
</script>