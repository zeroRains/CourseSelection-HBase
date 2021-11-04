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
      <el-table-column label="课号" prop="cno"> </el-table-column>
      <el-table-column label="名称" prop="name"> </el-table-column>
      <el-table-column label="学分" prop="credit"> </el-table-column>
      <el-table-column label="学年" prop="semester"> </el-table-column>
      <el-table-column label="老师" prop="teacher"> </el-table-column>
      <el-table-column label="职称" prop="grade"> </el-table-column>
      <el-table-column align="right">
        <template slot="header">
          <el-button @click="importFile" style="font-size: 20px" type="primary"
            >导入课程信息</el-button
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
export default {
  name: "DelCourseSchedule",
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
      alert("这里导入课程文件");
    },
  },
};
</script>