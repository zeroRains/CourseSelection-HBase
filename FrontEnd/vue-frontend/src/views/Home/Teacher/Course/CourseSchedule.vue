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
              action="http://111.229.52.254:9779/all/upload_file/info_type=student"
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              :before-remove="beforeRemove"
              multiple
              :limit="1"
              :on-exceed="handleExceed"
              :http-request="uploadFile"
          >
            <el-button @click="refresh" style="font-size: 20px" type="primary"
            >点击上传
            </el-button
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
    uploadFile(param) {
      let fileObj = param.file
      let form = new FormData()
      form.append("file", fileObj, fileObj.filename)
      console.log("==" + form.get("file"), fileObj, form)
      this.$axios.post("all/upload_file/info_type=course", form, {
        headers: {'Content-Type': 'multipart/form-data'}
      }).then(res => {
        location.reload()
      })
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed(files, fileList) {
      // this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
      console.log(files)
    },
    beforeRemove(file, fileList) {
      return "1111"
    }
  },
};
</script>
