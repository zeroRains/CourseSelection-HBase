<template>
  <div class="CourseSchedule">
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
          <!-- <el-button type="primary" @click="handleEdit">添加计划</el-button> -->
          <AddSchedule />
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import AddSchedule from "@/components/AddSchedule";
export default {
  name: "CourseSchedule",
  components: {
    AddSchedule,
  },
  data() {
    var tableData;
    this.$axios
      .get(
        "teacher/getCourseScheduleTable/userid=" +
          window.localStorage.getItem("userid")
      )
      .then((res) => {
        this.tableData = res.data.data;
        // console.log(this.tableData);
      });
    return {
      tableData,
    };
  },
  methods: {
    handleEdit() {
      console.log("");
    },
  },
};
</script>