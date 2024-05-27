<template>
  <div>
    <el-form :inline="true" :model="formInline" class="demo-form-inline">
      <el-form-item label="用户id">
        <el-input v-model="formInline.id" placeholder="id"></el-input>
      </el-form-item>
      <el-form-item label="用户名">
        <el-input v-model="formInline.username" placeholder="用户名"></el-input>
      </el-form-item>
      <el-form-item label="性别">
        <el-select v-model="formInline.region" placeholder="性别">
          <el-option label="男" value="shanghai"></el-option>
          <el-option label="女" value="beijing"></el-option>
          <el-option label="保密" value="beijing"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">查询</el-button>
      </el-form-item>
    </el-form>

<!--  导航菜单  -->
    <el-row class="tac">
      <el-col :span="4" style="margin-top: 5px;position: absolute">
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose">
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>任务管理系统</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1" @click="onClickUsers">用户管理</el-menu-item>
              <el-menu-item index="1-2" @click="onClickTasks">任务管理</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-col>
    </el-row>

    <!-- 用户管理表格 -->
    <el-table v-if="isVisible"
              :data="tableData"
              style="width: 80%; margin-left: 300px; margin-top: 5px;">
      <el-table-column
          label="id"
          prop="id"
          width="180">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="昵称"
          prop="name"
          width="180">
      </el-table-column>
      <el-table-column
          label="性别"
          prop="gender"
          width="180">
        <template v-slot="scope">
          <span style="margin-left: 10px">{{ scope.row.gender }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="电话"
          prop="telephone"
          width="180">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.telephone }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text"
              size="mini"
              @click="()=>{handleEdit(scope.$index, scope.row);dialogFormVisible = true}">编辑</el-button>
          <el-dialog title="修改信息" :visible.sync="dialogFormVisible">
            <el-form :model="editedData">
              <el-form-item label="username" :label-width="formLabelWidth">
                <el-input v-model="editedData.name" autocomplete="off" placeholder="请输入要修改的用户名"></el-input>
              </el-form-item>
<!--              <el-form-item label="username" :label-width="formLabelWidth">-->
<!--                <el-input v-model="editedData.username" autocomplete="off"></el-input>-->
<!--              </el-form-item>-->
              <el-form-item label="gender" :label-width="formLabelWidth">
                <el-input v-model="editedData.gender" autocomplete="off" placeholder="请输入要修改的性别(男，女，保密)">
                </el-input>
              </el-form-item>
              <el-form-item label="telephone" :label-width="formLabelWidth">
                <el-input v-model="editedData.telephone" autocomplete="off" placeholder="请输入要修改的电话号码"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
              <el-button type="primary" @click="()=>{dialogFormVisible = false;updateData()}">确 定</el-button>
            </div>
          </el-dialog>

          <el-button type="text"
              size="mini"
              @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
<!--标题-->
    <h1 v-if="isVisible1">欢迎来到任务管理系统</h1>

    <!-- 任务管理表格 -->
    <el-table v-if="isVisible2"
              :data="tableData2"
              style="width: 80%; margin-left: 220px; margin-top: 5px;">
      <el-table-column
          prop="id"
          label="id"
          width="80">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column
          prop="shortDescription"
          label="简要描述"
          width="200">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>简要描述: {{ scope.row.description }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.description }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column
          prop="detail"
          label="详细描述"
          width="220">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.detail }}</span>
        </template>
      </el-table-column>
      <el-table-column
          prop="type"
          label="类型"
          width="120">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.type }}</span>
        </template>
      </el-table-column>
      <el-table-column
          prop="price"
          label="任务酬劳"
          width="120">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.price }}</span>
        </template>
      </el-table-column>
      <el-table-column
          prop="publisher"
          label="任务发布人"
          width="120">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.publisher }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text"
                     size="mini"
                     @click="()=>{handleEdit1(scope.$index, scope.row);dialogFormVisible = true}">编辑</el-button>
          <el-dialog title="修改信息" :visible.sync="dialogFormVisible">
            <el-form :model="editedData1">
              <el-form-item label="description" :label-width="formLabelWidth">
                <el-input v-model="editedData1.description" autocomplete="off" placeholder="请输入要修改的用户名"></el-input>
              </el-form-item>
              <el-form-item label="detail" :label-width="formLabelWidth">
                <el-input v-model="editedData1.detail" autocomplete="off" placeholder="请输入要修改的性别(男，女，保密)">
                </el-input>
              </el-form-item>
              <el-form-item label="type" :label-width="formLabelWidth">
                <el-input v-model="editedData1.type" autocomplete="off" placeholder="请输入要修改的电话号码"></el-input>
              </el-form-item>
              <el-form-item label="price" :label-width="formLabelWidth">
                <el-input v-model="editedData1.price" autocomplete="off" placeholder="请输入要修改的电话号码"></el-input>
              </el-form-item>
              <el-form-item label="publisher" :label-width="formLabelWidth">
                <el-input v-model="editedData1.publisher" autocomplete="off" placeholder="请输入要修改的电话号码"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
              <el-button type="primary" @click="()=>{dialogFormVisible = false;updateData1()}">确 定</el-button>
            </div>
          </el-dialog>

          <el-button type="text"
                     size="mini"
                     @click="handleDelete1(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

  </div>


</template>

<script>
// 在需要发送 HTTP 请求的组件中引入 Axios
import axios from 'axios';
export default {
  data() {
    return {
      isVisible: false,
      isVisible1: true,
      isVisible2: false,
      isCollapse: true,
      dialogFormVisible: false,//dialog可视化
      formInline: {
        user: '',
        region: ''
      },
      tableData: [
        { id: 1, name: '测试用户1', gender: '男', telephone: '1234567890' },
        { id: 2, name: '测试用户2', gender: '女', telephone: '0987654321' }
      ],
      tableData2:[
        {id:1,description:'study',detail:'今天学一小时，明白学两小时，依次递增，每天依次循环',type:'学习',price:2000,publisher:1}
      ],
      editedData: {}, // 用于保存用户编辑后的数据
      editedData1: {}, // 用于保存任务编辑后的数据

    }
  },
  methods: {
    // 导航栏
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    //表格
    handleEdit(index, row) {
      this.editedData = { ...row }; // 使用对象解构复制数据，确保不改变原始数据
      this.dialogFormVisible = true;
      // console.log(index, row);
    },
    handleEdit1(index, row) {
      this.editedData1 = { ...row }; // 使用对象解构复制数据，确保不改变原始数据
      this.dialogFormVisible = true;
      // console.log(index, row);
    },
    handleDelete(index) {
      // 在这里可以添加逻辑以确认是否真的要删除
      // 以下示例直接从数据数组中删除该行记录
      this.tableData.splice(index, 1);
    },
    handleDelete1(index) {
      // 在这里可以添加逻辑以确认是否真的要删除
      // 以下示例直接从数据数组中删除该行记录
      this.tableData2.splice(index, 1);
    },
    onClickUsers(){
      //表格可视化
      this.isVisible = true;
      //标题可视化
      this.isVisible1 = false;
      this.isVisible2 = false;

    },
    onClickTasks(){
      //任务表格可视化
      this.isVisible2 = true;
    //表格可视化
      this.isVisible = false;
      //标题可视化
      this.isVisible1 = false;

    },
    updateData() {
      // 找到编辑的行在表格数据中的索引
      const index = this.tableData.findIndex(item => item.id === this.editedData.id);
      // 使用 Vue.set 方法更新数据，以确保响应式
      this.$set(this.tableData, index, this.editedData);
      // 关闭对话框
      this.dialogFormVisible = false;
    },
    updateData1() {
      // 找到编辑的行在表格数据中的索引
      const index = this.tableData2.findIndex(item => item.id === this.editedData1.id);
      // 使用 Vue.set 方法更新数据，以确保响应式
      this.$set(this.tableData2, index, this.editedData1);
      // 关闭对话框
      this.dialogFormVisible = false;
    },
    onSubmit() {
      // 构造请求数据
      const requestData = {
        id: this.formInline.id,
        username: this.formInline.username,
        gender: this.formInline.gender,
        telephone:this.formInline.telephone
      };


      // 发送 POST 请求到后端
      axios.post(`/users?id=${this.id}`, requestData)
          .then(response => {
            // 请求成功，处理后端返回的数据
            console.log('Response from server:', response.data);
          })
          .catch(error => {
            // 请求失败，处理错误情况
            console.error('Error:', error);
            // 在界面上显示错误消息
            this.$message.error('请求失败，请稍后重试！');
          });
    },
    fetchData() {
      axios.get('/users') // 确保这个 URL 和你的后端 API 地址匹配
          .then(response => {
            this.tableData = response.data;
          })
          .catch(error => {
            console.error('Error fetching data:', error);
            // 在界面上显示错误消息
            this.$message.error('请求失败，请稍后重试！');
          });
    }
  }
}

</script>

<style>
.el-dropdown-link {
  cursor: pointer;
  color: #409EFF;
}
.el-icon-arrow-down {
  font-size: 12px;
}
</style>

