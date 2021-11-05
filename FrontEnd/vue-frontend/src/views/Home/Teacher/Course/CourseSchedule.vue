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
      <el-table-column align="center" label="学号" prop="sno">
      </el-table-column>
      <el-table-column align="center" label="姓名" prop="name">
      </el-table-column>
      <el-table-column align="center" label="性别" prop="sex">
      </el-table-column>
      <el-table-column align="center" label="年龄" prop="age">
      </el-table-column>
      <el-table-column align="center" label="学院" prop="department">
      </el-table-column>
      <el-table-column align="center" label="专业" prop="major">
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
            <el-button @click="refresh" style="font-size: 20px" type="primary"
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
  name: "CourseSchedule",

  data() {
    var tableData = [];
    // close.log(tableData);
    this.$axios.get("all/getAllStudent").then((res) => {
      var temp = res.data.data;
      console.log(temp);
      for (let a of temp) {
        // console.log(a.coursecode);
        this.tableData.push({
          sno: a.sno,
          name: a.sname,
          sex: a.sex,
          age: a.age,
          department: a.department,
          major: a.major,
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
    refresh() {
      // alert("test");
    },
  },
};
</script>