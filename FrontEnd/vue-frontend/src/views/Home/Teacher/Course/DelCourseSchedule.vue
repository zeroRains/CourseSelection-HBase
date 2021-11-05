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
      <el-table-column align="center" label="课号" prop="cno">
      </el-table-column>
      <el-table-column align="center" label="名称" prop="name">
      </el-table-column>
      <el-table-column align="center" label="学分" prop="credit">
      </el-table-column>
      <el-table-column align="center" label="学年" prop="semester">
      </el-table-column>
      <el-table-column align="center" label="老师" prop="teacher">
      </el-table-column>
      <el-table-column align="center" label="职称" prop="grade">
      </el-table-column>
      <el-table-column align="center">
        <template slot="header">
          <el-upload
            class="upload-demo"
            action="https://jsonplaceholder.typicode.com/posts/"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            multiple
            :limit="3"
            :on-exceed="handleExceed"
            :file-list="fileList"
          >
            <el-button style="font-size: 20px" type="primary"
              >点击上传</el-button
            >
          </el-upload>
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
    this.$axios.get("all/getAllCourse").then((res) => {
      var temp = res.data.data;
      console.log(temp);
      for (let a of temp) {
        // console.log(a.coursecode);
        this.tableData.push({
          cno: a.cno,
          name: a.cname,
          credit: a.credit,
          grade: a.grade,
          semester: a.semester,
          teacher: a.teacher,
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
  },
};
</script>