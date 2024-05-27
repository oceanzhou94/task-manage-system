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
      <el-col :span="3" style="margin-top: 5px;position: absolute">
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

    <!--    table用户管理表格-->
    <el-table v-if="isVisible"
              :data="tableData"
              style="width: 60%;margin-left: 260px;margin-top: 5px;">
      <el-table-column
          label="id"
          width="180">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="昵称"
          width="180">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>姓名: {{ scope.row.name }}</p>
            <p>住址: {{ scope.row.address }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.name }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column
          label="密码"
          width="180">
        <template v-slot="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="性别"
          width="180">
        <template v-slot="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="电话"
          width="180">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
        </template>
      </el-table-column>

    </el-table>
    <!--标题-->
    <h1 v-if="isVisible1">欢迎来到任务管理系统</h1>

    <!--    table任务管理-->
    <el-table v-if="isVisible2"
              :data="tableData"
              style="width: 60%;margin-left: 260px;margin-top: 5px;">
      <el-table-column
          label="id"
          width="180">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="简要描述"
          width="200">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>姓名: {{ scope.row.name }}</p>
            <p>住址: {{ scope.row.address }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.name }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column
          label="详细描述"
          width="220">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="类型"
          width="120">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="任务酬劳"
          width="120">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="任务发布人"
          width="120">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.date }}</span>
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
      isVisible1:true,
      isVisible2:false,
      isCollapse: true,
      formInline: {
        user: '',
        region: ''
      }
    }
  },
  tableData: [{

  }],

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
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
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
    onSubmit() {
      // 构造请求数据
      const requestData = {
        id: this.formInline.id,
        username: this.formInline.username,
        gender: this.formInline.gender
      };


      // 发送 POST 请求到后端
      axios.post('/users?id=${this.id}', requestData)
          .then(response => {
            // 请求成功，处理后端返回的数据
            console.log('Response from server:', response.data);
          })
          .catch(error => {
            // 请求失败，处理错误情况
            console.error('Error:', error);
          });
    },
    fetchData() {
      axios.get('/users') // 确保这个 URL 和你的后端 API 地址匹配
          .then(response => {
            this.tableData = response.data;
          })
          .catch(error => {
            console.error('Error fetching data:', error);
          });
    }
  }
}
</script>

<style>

</style>