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
      <el-table-column label="姓名" prop="name"> </el-table-column>
      <el-table-column label="学号" prop="sno"> </el-table-column>
      <el-table-column label="性别" prop="sex"> </el-table-column>
      <el-table-column label="年龄" prop="age"> </el-table-column>
      <el-table-column label="学院" prop="department"> </el-table-column>
      <el-table-column label="专业" prop="major"> </el-table-column>
      <el-table-column align="right">
        <template slot="header">
          <el-button @click="importFile" style="font-size: 20px" type="primary"
            >导入学生成绩</el-button
          >
        </template>
        <template slot-scope="test">
          <div
            style="width: 40px; height: 40px"
            @mousedown="handleEdit(test.$index, test.row)"
          >
            <AddSchedule :position="position" />
          </div>
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
    var tableData = [];
    // close.log(tableData);
    this.$axios
      .get("stu/getCourseTable/userid=" + window.localStorage.getItem("userid"))
      .then((res) => {
        var temp = res.data.data;
        console.log(temp);
        for (let a of temp) {
          // console.log(a.coursecode);
          this.tableData.push({
            name: a.name,
            date: a.cno,
            credit: a.credit,
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
      // console.log(index);
      // alert(row);
      this.position = row.date;
      console.log(row);
      // alert(index, row);
      // console.log(row);
      // alert(row.credit);
      // console.log(index, row);
    },
    importFile() {
      alert("这里导入文件");
    },
  },
};
</script>