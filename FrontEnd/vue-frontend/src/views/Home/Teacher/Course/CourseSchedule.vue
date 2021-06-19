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
      <el-table-column label="课程序号" prop="date"> </el-table-column>
      <el-table-column label="课程代码" prop="name"> </el-table-column>
      <el-table-column label="课程名称" prop="name"> </el-table-column>
      <el-table-column label="开始周" prop="name"> </el-table-column>
      <el-table-column label="结束周" prop="name"> </el-table-column>
      <el-table-column label="星期" prop="name"> </el-table-column>
      <el-table-column label="节次" prop="name"> </el-table-column>
      <el-table-column label="学分" prop="name"> </el-table-column>
      <el-table-column label="教室" prop="name"> </el-table-column>
      <el-table-column label="可选人数" prop="name"> </el-table-column>
      <el-table-column label="已选人数" prop="name"> </el-table-column>
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
    var course = this.$axios.get().then((res) => {
      console.log(res);
    });
    return {
      course,
      tableData: [
        {
          date: "2016-05-02",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄",
        },
        {
          date: "2016-05-04",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1517 弄",
        },
        {
          date: "2016-05-01",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1519 弄",
        },
        {
          date: "2016-05-03",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1516 弄",
        },
      ],
    };
  },
  methods: {
    handleEdit() {
      console.log("");
    },
  },
};
</script>