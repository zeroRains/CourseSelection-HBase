<template>
  <div class="Info">
    <!-- <div class="container">
      <el-table
        :show-header="false"
        :data="tableData"
        border
        style="width: 100%"
      >
        <el-table-column align="center" prop="date" label="" width="200">
        </el-table-column>
        <el-table-column align="center" prop="name" label="" width="200">
        </el-table-column>
      </el-table>
    </div> -->
    <div class="container">
      <el-form label-width="80px" :model="formLabelAlign">
        <el-form-item label="姓名">
          <el-input v-model="formLabelAlign.tname"></el-input>
        </el-form-item>
        <el-form-item label="工号">
          <el-input disabled v-model="formLabelAlign.tno"></el-input>
        </el-form-item>
        <el-form-item label="性别">
          <el-input v-model="formLabelAlign.sex"></el-input>
        </el-form-item>
        <el-form-item label="年龄">
          <el-input v-model="formLabelAlign.age"></el-input>
        </el-form-item>
        <el-form-item label="出生日期">
          <el-input v-model="formLabelAlign.birthday"></el-input>
        </el-form-item>
        <el-form-item label="学院">
          <el-input disabled v-model="formLabelAlign.college_name"></el-input>
        </el-form-item>
        <el-form-item label="职位">
          <el-input v-model="formLabelAlign.position"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="changedate">修改</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import "@/assets/info.css";
export default {
  name: "Info",
  data() {
    // var tableData;
    var formLabelAlign;
    this.$axios
      .post(
        "teacher/getTeacherInfo/userid=" + window.localStorage.getItem("userid")
      )
      .then((res) => {
        var temp = res.data.data[0];
        this.formLabelAlign = {
          tname: temp.tname,
          tno: temp.tno,
          sex: temp.sex,
          age: temp.age,
          birthday: String(temp.birthday.split(" ")[0]),
          college_name: temp.college_name,
          position: temp.position,
        };
        // alert();
        // this.tableData = [
        //   {
        //     date: "姓名",
        //     name: temp.tname,
        //   },
        //   {
        //     date: "工号",
        //     name: temp.tno,
        //   },
        //   {
        //     date: "性别",
        //     name: temp.sex,
        //   },
        //   {
        //     date: "年龄",
        //     name: temp.age,
        //   },
        //   {
        //     date: "出生日期",
        //     name: String(temp.birthday.split(" ")[0]),
        //   },

        //   {
        //     date: "学院",
        //     name: temp.college_name,
        //   },
        //   {
        //     date: "职位",
        //     name: temp.position,
        //   },
        // ];
      });
    return {
      // tableData,
      formLabelAlign,
    };
  },
  methods: {
    changedate() {
      var info = this.formLabelAlign;
      var name = `${info.tname},${info.sex},${info.age},${info.birthday},${info.position}`;
      // alert(name);
      // // alert(name);
      this.$axios
        .post(
          "teacher/updateTeacherInfo/userid=" +
            window.localStorage.getItem("userid") +
            "&info=" +
            name
        )
        .then((res) => {
          console.log(res);
          if (res.data.status == "success") {
            this.$message({
              message: "修改成功",
              type: "success",
            });
            location.reload();
          } else {
            this.$message.error("修改失败！");
          }
        });
    },
  },
};
</script>

<style  scoped>
.container {
  width: 401px;
}
</style>