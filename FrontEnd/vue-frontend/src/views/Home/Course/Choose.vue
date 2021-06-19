<template>
  <div class="Choose">
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
      <el-table-column label="课程名称" prop="name"> </el-table-column>
      <el-table-column label="课程代号" prop="date"> </el-table-column>
      <el-table-column label="学分" prop="credit"> </el-table-column>
      <el-table-column align="right">
        <template slot="header">
          <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
        </template>
        <template slot-scope="test">
          <div
            style="width: 40px; height: 40px"
            @mousedown="handleEdit(test.$index, test.row)"
          >
            <Selected :position="position" />
          </div>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import Selected from "@/components/Selected.vue";
export default {
  name: "Choose",
  components: {
    Selected,
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
  },
};
</script>
<style lang="scss" scoped>
.el-table__header {
  height: 40px;
}
</style>