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
        <el-select v-model="formInline.gender" placeholder="性别">
          <el-option label="男" value="male"></el-option>
          <el-option label="女" value="female"></el-option>
          <el-option label="保密" value="secret"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">查询</el-button>
      </el-form-item>
    </el-form>

    <!-- 导航菜单 -->
    <el-row class="tac">
      <el-col :span="3" style="margin-top: 5px;position: absolute">
        <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
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
    <div v-if="isVisible">
      <el-button type="primary" @click="dialogAddUserVisible = true;">添加用户</el-button>
    <el-table :data="tableUserData" style="width: 80%;margin-left: 260px;margin-top: 5px;">
      <el-table-column label="id" width="180">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="昵称" width="180">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.username }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="密码" width="180">
        <template v-slot="scope">
          <span style="margin-left: 10px">{{ scope.row.password }}</span>
        </template>
      </el-table-column>
      <el-table-column label="性别" width="180">
        <template v-slot="scope">
          <span style="margin-left: 10px">{{ scope.row.gender }}</span>
        </template>
      </el-table-column>
      <el-table-column label="电话" width="180">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.phone }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text" size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button type="text" size="mini" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    </div>

    <!-- 标题 -->
    <h1 v-if="isVisible1">欢迎来到任务管理系统</h1>

    <!-- 任务管理表格 -->
    <div v-if="isVisible2">
      <el-button type="primary" @click="dialogAddTaskVisible = true;">添加任务</el-button>
    <el-table  :data="tableTaskData" style="width: 80%;margin-left: 260px;margin-top: 5px;">
      <el-table-column label="id" width="180">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.id }}</span>
        </template>
      </el-table-column>

      <el-table-column label="简要描述" width="200">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>描述: {{ scope.row.description }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.description }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="详细描述" width="220">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.detail }}</span>
        </template>
      </el-table-column>
      <el-table-column label="类型" width="120">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.type }}</span>
        </template>
      </el-table-column>
      <el-table-column label="任务酬劳" width="120">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.price }}</span>
        </template>
      </el-table-column>
<!--      <el-table-column label="任务发布人" width="120">-->
<!--        <template slot-scope="scope">-->
<!--          <span style="margin-left: 10px">{{ scope.row.publisher_id }}</span>-->
<!--        </template>-->
<!--      </el-table-column>-->
      <el-table-column label="创建时间" width="200">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>描述: {{ scope.row.created_time }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.created_time }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="更新时间" width="200">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>描述: {{ scope.row.updated_time }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.updated_time }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text" size="mini" @click="handleEdit1(scope.$index, scope.row)">编辑</el-button>
<!--          <el-button type="text" size="mini" @click="handleDelete1(scope.$index, scope.row)">删除</el-button>-->
          <el-button type="text" size="mini" @click="deleteUser(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    </div>

    <!-- 编辑用户对话框 -->
    <el-dialog title="修改信息" :visible.sync="dialogEditUserVisible">
      <el-form :model="editedData">
        <el-form-item label="用户名" :label-width="formLabelWidth">
          <el-input v-model="editedData.name" autocomplete="off" placeholder="请输入要修改的用户名"></el-input>
        </el-form-item>
        <el-form-item label="性别" :label-width="formLabelWidth">
          <el-input v-model="editedData.gender" autocomplete="off" placeholder="请输入性别"></el-input>
        </el-form-item>
        <el-form-item label="电话" :label-width="formLabelWidth">
          <el-input v-model="editedData.telephone" autocomplete="off" placeholder="请输入电话号码"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogEditUserVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateUser">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 编辑任务对话框 -->
    <el-dialog title="修改任务" :visible.sync="dialogEditTaskVisible">
      <el-form :model="editedTask">
        <el-form-item label="简要描述" :label-width="formLabelWidth">
          <el-input v-model="editedTask.description" autocomplete="off" placeholder="请输入要修改的简要描述"></el-input>
        </el-form-item>
        <el-form-item label="详细描述" :label-width="formLabelWidth">
          <el-input v-model="editedTask.detail" autocomplete="off" placeholder="请输入详细描述"></el-input>
        </el-form-item>
        <el-form-item label="类型" :label-width="formLabelWidth">
          <el-input v-model="editedTask.type" autocomplete="off" placeholder="请输入任务类型"></el-input>
        </el-form-item>
        <el-form-item label="任务酬劳" :label-width="formLabelWidth">
          <el-input v-model="editedTask.price" autocomplete="off" placeholder="请输入任务酬劳"></el-input>
        </el-form-item>
<!--        <el-form-item label="任务发布人" :label-width="formLabelWidth">-->
<!--          <el-input v-model="editedTask.publisher_id" autocomplete="off" placeholder="请输入任务发布人"></el-input>-->
<!--        </el-form-item>-->
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogEditTaskVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateTask">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 添加用户对话框 -->
    <el-dialog title="添加用户" :visible.sync="dialogAddUserVisible">
      <el-form :model="newUser">
        <el-form-item label="id" :label-width="formLabelWidth">
          <el-input v-model="newUser.id" autocomplete="off" placeholder="请输入id"></el-input>
        </el-form-item>
        <el-form-item label="用户名" :label-width="formLabelWidth">
          <el-input v-model="newUser.username" autocomplete="off" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" :label-width="formLabelWidth">
          <el-input v-model="newUser.password" autocomplete="off" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item label="性别" :label-width="formLabelWidth">
          <el-input v-model="newUser.gender" autocomplete="off" placeholder="请输入性别"></el-input>
        </el-form-item>
        <el-form-item label="电话" :label-width="formLabelWidth">
          <el-input v-model="newUser.phone" autocomplete="off" placeholder="请输入电话号码"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogAddUserVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUser">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 添加任务对话框 -->
    <el-dialog title="添加任务" :visible.sync="dialogAddTaskVisible">
      <el-form :model="newTask">、
        <el-form-item label="id" :label-width="formLabelWidth">
          <el-input v-model="newTask.id" autocomplete="off" placeholder="请输入id"></el-input>
        </el-form-item>
        <el-form-item label="简要描述" :label-width="formLabelWidth">
          <el-input v-model="newTask.description" autocomplete="off" placeholder="请输入简要描述"></el-input>
        </el-form-item>
        <el-form-item label="详细描述" :label-width="formLabelWidth">
          <el-input v-model="newTask.detail" autocomplete="off" placeholder="请输入详细描述"></el-input>
        </el-form-item>
        <el-form-item label="类型" :label-width="formLabelWidth">
          <el-input v-model="newTask.type" autocomplete="off" placeholder="请输入任务类型"></el-input>
        </el-form-item>
        <el-form-item label="任务酬劳" :label-width="formLabelWidth">
          <el-input v-model="newTask.price" autocomplete="off" placeholder="请输入任务酬劳"></el-input>
        </el-form-item>
        <el-form-item label="任务发布人" :label-width="formLabelWidth">
          <el-input v-model="newTask.publisher_id" autocomplete="off" placeholder="请输入任务发布人"></el-input>
        </el-form-item>
        <el-form-item label="创建时间" :label-width="formLabelWidth">
          <el-input v-model="newTask.created_time" autocomplete="off" placeholder="请输入创建时间"></el-input>
        </el-form-item>
        <el-form-item label="更新时间" :label-width="formLabelWidth">
          <el-input v-model="newTask.updated_time" autocomplete="off" placeholder="请输入更新时间"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogAddTaskVisible = false">取 消</el-button>
        <el-button type="primary" @click="addTask">确 定</el-button>
      </div>
    </el-dialog>


  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isVisible: false,
      isVisible1: true,
      isVisible2: false,
      dialogAddUserVisible: false,
      dialogAddTaskVisible: false,
      dialogEditUserVisible: false,
      dialogEditTaskVisible: false,
      // isCollapse: true,
      formInline: {
        id: '',
        username: '',
        gender: ''
      },
      newUser: {
        id:'',
        username: '',
        gender: '',
        phone: '',
      },
      newTask: {
        id:'',
        description: '',
        detail: '',
        type: '',
        price: '',
        publisher_id: '',
        created_time:'',
        updated_time:'',
      },
      tableUserData: [],
      tableTaskData: [],
      editedData: {},//编辑后的用户data
      editedTask: {}//编辑后的任务data
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    onClickUsers() {
      this.isVisible = true;
      this.isVisible1 = false;
      this.isVisible2 = false;
      this.fetchUserData();
    },
    onClickTasks() {
      this.isVisible2 = true;
      this.isVisible = false;
      this.isVisible1 = false;
      this.fetchTaskData();
    },
    handleEdit(index, row) {
      this.editedData = {...row};
      this.dialogEditUserVisible = true;
    },
    handleEdit1(index, row) {
      this.editedTask = {...row};
      this.dialogEditTaskVisible = true;
    },
    handleDelete(index) {
      this.tableUserData.splice(index, 1);
    },
    handleDelete1(index) {
      this.tableTaskData.splice(index, 1);
    },
    updateUser() {
      const index = this.tableUserData.findIndex(user => user.id === this.editedData.id);
      if (index !== -1) {
        this.tableUserData.splice(index, 1, this.editedData);
      }
      this.dialogEditUserVisible = false;
    },
    updateTask() {
      const index = this.tableTaskData.findIndex(task => task.id === this.editedTask.id);
      if (index !== -1) {
        this.tableTaskData.splice(index, 1, this.editedTask);
      }
      this.dialogEditTaskVisible = false;
    },
    // addUser() {
    //   this.tableUserData.push({...this.newUser});
    //   this.dialogAddUserVisible = false;
    // },
    //添加用户
    addUser() {
      // 构建要发送到服务器端的用户数据
      const userData = {
        id: this.newUser.id,
        username: this.newUser.username,
        gender: this.newUser.gender,
        phone: this.newUser.phone
      };

      // 发送HTTP POST请求到服务器端保存用户数据
      axios.post('http://服务器地址/保存用户数据的接口路径', userData)
          .then(response => {
            // 如果保存成功，将新用户数据添加到前端的数据列表中
            this.tableUserData.push(response.data); // 假设服务器返回了保存成功的用户数据
            this.dialogAddUserVisible = false; // 关闭添加用户对话框
          })
          .catch(error => {
            console.error('Error adding user:', error);
            // 处理保存失败的情况，例如显示错误信息给用户
          });
    },
    //添加任务
    addTask() {
      // 构建要发送到服务器端的用户数据
      const taskData = {
        id: this.newTask.id,
        description: this.newTask.description,
        detail: this.newTask.detail,
        type: this.newTask.type,
        price: this.newTask.price,
        publisher_id: this.newTask.publisher_id,
        created_time: this.newTask.created_time,
        updated_time: this.newTask.pupdated_time
      };

      // 发送HTTP POST请求到服务器端保存用户数据
      axios.post('http://服务器地址/保存用户数据的接口路径', taskData)
          .then(response => {
            // 如果保存成功，将新用户数据添加到前端的数据列表中
            this.tableTaskData.push(response.data); // 假设服务器返回了保存成功的用户数据
            this.dialogAddTaskVisible = false; // 关闭添加用户对话框
          })
          .catch(error => {
            console.error('Error adding user:', error);
            // 处理保存失败的情况，例如显示错误信息给用户
          });
    },
    onSubmit() {
      const requestData = {
        id: this.formInline.id,
        username: this.formInline.username,
        gender: this.formInline.gender
      };

      //根据用户的id进行查询
      axios.post(`/users?id=${this.formInline.id}`, requestData)
          .then(response => {
            console.log('Response from server:', response.data);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    },
    //根据
    //获取任务的全部数据
    fetchTaskData() {
      console.log('Fetching task data...'); // 增加日志
      axios.get('http://192.168.184.1:8000/tms/task/list')
          .then(response => {
            console.log('Task data fetched:', response.data.data.tasks); // Log the response data
            this.tableTaskData = response.data.data.tasks; // 确保数据路径正确
          })
          .catch(error => {
            console.error('Error fetching task data:', error);
            if (error.response) {
              console.error('Error response data:', error.response.data);
            }
          });
    },
    //获取用户的全部数据
    fetchUserData() {
      axios.get('http://localhost:8000/tms/user/list')
          .then(response => {
            console.log('User data fetched:', response.data); // Log the response data
            this.tableUserData = response.data.data.users; // Ensure data path is correct
          })
          .catch(error => {
            console.error('Error fetching user data:', error);
          });
    },
    // 删除用户
    deleteUser(id) {
      // 发送 HTTP DELETE 请求到服务器端删除用户
      axios.delete(`http://服务器地址/删除用户的接口路径/${id}`)
          .then(response => {
            console.log('User deleted successfully:', response.data);
            // 在前端删除相应的用户数据
            const index = this.tableUserData.findIndex(user => user.id === id);
            if (index !== -1) {
              this.tableUserData.splice(index, 1);
            }
          })
          .catch(error => {
            console.error('Error deleting user:', error);
            // 处理删除失败的情况，例如显示错误信息给用户
          });
    },
    // 删除任务
    deleteTask(id) {
      // 发送 HTTP DELETE 请求到服务器端删除任务
      axios.delete(`http://服务器地址/删除任务的接口路径/${id}`)
          .then(response => {
            console.log('Task deleted successfully:', response.data);
            // 在前端删除相应的任务数据
            const index = this.tableTaskData.findIndex(task => task.id === id);
            if (index !== -1) {
              this.tableTaskData.splice(index, 1);
            }
          })
          .catch(error => {
            console.error('Error deleting task:', error);
            // 处理删除失败的情况，例如显示错误信息给用户
          });
    }
  }
};
</script>

<style>
</style>
