<template>
  <div class="Change">
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
      <el-table-column align="center" label="课程代码" prop="coursecode">
      </el-table-column>
      <el-table-column align="center" label="课程名称" prop="name">
      </el-table-column>
      <el-table-column align="center" label="开始周" prop="startweek">
      </el-table-column>
      <el-table-column align="center" label="结束周" prop="endweek">
      </el-table-column>
      <el-table-column align="center" label="星期" prop="day">
      </el-table-column>
      <el-table-column align="center" label="节次" prop="index">
      </el-table-column>
      <el-table-column align="center" label="教室" prop="classroom">
      </el-table-column>
      <el-table-column align="center" label="可选人数" prop="optional">
      </el-table-column>
      <el-table-column align="center" label="已选人数" prop="selected">
      </el-table-column>
      <el-table-column align="right">
        <template slot="header">
          <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "Change",
  data() {
    var tableData;
    this.$axios.get("/all/getCourseScheduleTable").then((res) => {
      this.tableData = res.data.data;
      console.log(this.tableData);
    });
    return {
      search: "",
      tableData,
    };
  },
};
</script>