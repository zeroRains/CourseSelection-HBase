<template>
  <div class="Selected">
    <el-button type="primary" @click="getPostion">选课</el-button>
    <el-dialog
      :customClass="customWidth"
      title="课程选择"
      :visible.sync="dialogTableVisible"
    >
      <el-table :data="tableData" style="width: 100%">
        <el-table-column label="课程序号">
          <template slot-scope="scope">
            <span>{{ scope.row.cno }}</span>
          </template>
        </el-table-column>
        <el-table-column label="课程代号">
          <template>
            <span>{{ this.position }}</span>
          </template>
        </el-table-column>
        <el-table-column label="课程名称">
          <template slot-scope="scope">
            <span>{{ scope.row.cname }}</span>
          </template>
        </el-table-column>
        <el-table-column label="开课周">
          <template slot-scope="scope">
            <span>{{ scope.row.startweek }}</span>
          </template>
        </el-table-column>
        <el-table-column label="结束周">
          <template slot-scope="scope">
            <span>{{ scope.row.endweek }}</span>
          </template>
        </el-table-column>
        <el-table-column label="星期">
          <template slot-scope="scope">
            <span>{{ scope.row.day }}</span>
          </template>
        </el-table-column>
        <el-table-column label="节次">
          <template slot-scope="scope">
            <span>{{ scope.row.index }}</span>
          </template>
        </el-table-column>
        <el-table-column label="授课教师">
          <template slot-scope="scope">
            <span>{{ scope.row.tname }}</span>
          </template>
        </el-table-column>
        <el-table-column label="可选人数">
          <template slot-scope="scope">
            <span>{{ scope.row.optional }}</span>
          </template>
        </el-table-column>
        <el-table-column label="已选人数">
          <template slot-scope="scope">
            <span>{{ scope.row.selected }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              type="primary"
              size="mini"
              @click="handleEdit(scope.$index, scope.row)"
              >选课</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>
<script>
export default {
  name: "Selected",
  props: {
    position: [],
  },
  data() {
    var tableData;

    return {
      dialogTableVisible: false,
      tableData,
    };
  },
  methods: {
    handleEdit(index, row) {
      this.$axios
        .post(
          "/stu/selectCourse/userid=" +
            window.localStorage.getItem("userid") +
            "&cno=" +
            row.cno
        )
        .then((res) => {
          if (res.data.status == "success") {
            this.$message({
              message: "选课成功！",
              type: "success",
            });
            this.dialogTableVisible = false;
          } else {
            this.$message.error("课程冲突，选择失败！");
          }
        });
    },
    getPostion() {
      this.$axios
        .get("stu/isChoosible/coursecode=" + this.position)
        .then((res) => {
          var temp = res.data.data;

          if (temp.length != 0) {
            this.tableData = temp;
            this.dialogTableVisible = true;
          } else {
            this.$message.error("当前课程没有可选的课号！");
          }
        });
      // alert(this.position);
    },
  },
};
</script>

<style>
.customWidth {
  width: 90%;
  height: 70%;
}
</style>