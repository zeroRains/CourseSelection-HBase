<template>
  <div class="Info">
    <div class="container">
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
    </div>
  </div>
</template>

<script>
import "@/assets/info.css";
export default {
  name: "Info",
  data() {
    var tableData;
    this.$axios
      .post(
        "teacher/getTeacherInfo/userid=" + window.localStorage.getItem("userid")
      )
      .then((res) => {
        var temp = res.data.data[0];
        // alert();
        this.tableData = [
          {
            date: "姓名",
            name: temp.tname,
          },
          {
            date: "工号",
            name: temp.tno,
          },
          {
            date: "性别",
            name: temp.sex,
          },
          {
            date: "年龄",
            name: temp.age,
          },
          {
            date: "出生日期",
            name: String(temp.birthday.split(" ")[0]),
          },

          {
            date: "学院",
            name: temp.college_name,
          },
          {
            date: "职位",
            name: temp.position,
          },
        ];
      });
    return {
      tableData,
    };
  },
};
</script>

<style  scoped>
.container {
  width: 401px;
}
</style>