<template>
  <div class="AddSchedule">
    <el-button type="primary" @click="dialogFormVisible = true"
      >添加课程计划</el-button
    >
    <el-dialog
      top="20px"
      customClass="customWidth1"
      title="创建课程计划"
      :visible.sync="dialogFormVisible"
    >
      <div>
        <el-form :model="form">
          <el-form-item label="课程序号" :label-width="formLabelWidth">
            <el-input
              placeholder="请输入课程序号"
              v-model="form.cno"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="课程名称" :label-width="formLabelWidth">
            <el-select
              @change="matchData"
              v-model="form.name"
              placeholder="请选择课程名称"
            >
              <el-option
                v-for="item in courselist"
                :key="item.coursecode"
                :label="item.name"
                :value="item"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="课程代码" :label-width="formLabelWidth">
            <el-input
              placeholder="请输入课程代码"
              v-model="form.coursecode"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="授课学期" :label-width="formLabelWidth">
            <el-select v-model="form.semester" placeholder="请选择授课学期">
              <el-option label="2020-2021下" value="2020-2021下"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="开始周" :label-width="formLabelWidth">
            <el-input
              type="number"
              placeholder="请输入开始周"
              v-model="form.startweek"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="结束周" :label-width="formLabelWidth">
            <el-input
              type="number"
              placeholder="请输入结束周"
              v-model="form.endweek"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="星期" :label-width="formLabelWidth">
            <el-input
              type="number"
              placeholder="请输入星期"
              v-model="form.day"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="节次" :label-width="formLabelWidth">
            <el-input
              type="number"
              placeholder="请输入节次"
              v-model="form.index"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="可选人数" :label-width="formLabelWidth">
            <el-input
              type="number"
              placeholder="请输入可选人数"
              v-model="form.option"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="教室" :label-width="formLabelWidth">
            <el-input
              placeholder="请输入教室"
              v-model="form.classroom"
              autocomplete="off"
            ></el-input>
          </el-form-item>
        </el-form>
      </div>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="check">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "AddSchedule",
  data() {
    var courselist;
    this.$axios.get("/all/getCourseTable").then((res) => {
      this.courselist = res.data.data;
    });
    return {
      courselist,
      isReload: false,
      dialogFormVisible: false,
      form: {
        cno: "",
        coursecode: "",
        name: "",
        semester: "",
        startweek: "",
        endweek: "",
        day: "",
        index: "",
        option: "",
        classroom: "",
      },
      formLabelWidth: "100px",
    };
  },

  methods: {
    handleEdit() {
      console.log("");
    },
    matchData() {
      this.form.coursecode = this.form.name.cno;
      this.form.name = this.form.name.name;
    },
    check() {
      this.$axios
        .post(
          "teacher/addNewCourseSchedule/userid=" +
            window.localStorage.getItem("userid") +
            "&cno=" +
            this.form.cno +
            "&coursecode=" +
            this.form.coursecode +
            "&semester=" +
            this.form.semester +
            "&classroom=" +
            this.form.classroom +
            "&time=" +
            this.form.day +
            "," +
            this.form.index +
            "," +
            this.form.startweek +
            "," +
            this.form.endweek +
            "&optional=" +
            this.form.option
        )
        .then((res) => {
          if (res.data.status == "success") {
            this.$message({
              message: "添加课程计划成功",
              type: "success",
            });
            location.reload();
          } else {
            this.$message.error("存在课程冲突，添加课程计划失败");
          }
        });
    },
  },
};
</script>
<style>
.customWidth1 {
  width: 500px;
  background: #e2e4e3;
}
</style>