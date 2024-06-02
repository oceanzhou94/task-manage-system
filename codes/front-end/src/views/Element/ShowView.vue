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

    <!-- 导航菜单 -->
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
    <div v-if="isVisible">
      <el-button type="primary" @click="dialogAddUserVisible = true;">添加用户</el-button>
      <el-table :data="tableData" style="width: 80%; margin-left: 300px; margin-top: 5px;">
        <el-table-column label="id" prop="id" width="180">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.id }}</span>
          </template>
        </el-table-column>
        <el-table-column label="昵称" prop="name" width="180"></el-table-column>
        <el-table-column label="性别" prop="gender" width="180">
          <template v-slot="scope">
            <span style="margin-left: 10px">{{ scope.row.gender }}</span>
          </template>
        </el-table-column>
        <el-table-column label="电话" prop="telephone" width="180">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.telephone }}</span>
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

    <!-- 任务管理表格 -->
    <div v-if="isVisible2">
      <el-button type="primary" @click="dialogAddTaskVisible = true;">添加任务</el-button>
      <el-table :data="tableData2" style="width: 80%; margin-left: 300px; margin-top: 5px;">
        <el-table-column prop="id" label="id" width="180">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.id }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="shortDescription" label="简要描述" width="200">
          <template slot-scope="scope">
            <el-popover trigger="hover" placement="top">
              <p>简要描述: {{ scope.row.description }}</p>
              <div slot="reference" class="name-wrapper">
                <el-tag size="medium">{{ scope.row.description }}</el-tag>
              </div>
            </el-popover>
          </template>
        </el-table-column>
        <el-table-column prop="detail" label="详细描述" width="220">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.detail }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="type" label="类型" width="120">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.type }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="price" label="任务酬劳" width="120">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.price }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="publisher" label="任务发布人" width="120">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.publisher }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="text" size="mini" @click="handleEdit1(scope.$index, scope.row)">编辑</el-button>
            <el-button type="text" size="mini" @click="handleDelete1(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 添加用户对话框 -->
    <el-dialog title="添加用户" :visible.sync="dialogAddUserVisible">
      <el-form :model="newUser">
        <el-form-item label="用户名" :label-width="formLabelWidth">
          <el-input v-model="newUser.name" autocomplete="off" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="性别" :label-width="formLabelWidth">
          <el-input v-model="newUser.gender" autocomplete="off" placeholder="请输入性别"></el-input>
        </el-form-item>
        <el-form-item label="电话" :label-width="formLabelWidth">
          <el-input v-model="newUser.telephone" autocomplete="off" placeholder="请输入电话号码"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogAddUserVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUser">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 添加任务对话框 -->
    <el-dialog title="添加任务" :visible.sync="dialogAddTaskVisible">
      <el-form :model="newTask">
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
          <el-input v-model="newTask.publisher" autocomplete="off" placeholder="请输入任务发布人"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogAddTaskVisible = false">取 消</el-button>
        <el-button type="primary" @click="addTask">确 定</el-button>
      </div>
    </el-dialog>

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
        <el-form-item label="任务发布人" :label-width="formLabelWidth">
          <el-input v-model="editedTask.publisher" autocomplete="off" placeholder="请输入任务发布人"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogEditTaskVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateTask">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formInline: {
        id: '',
        username: '',
        region: '',
      },
      tableData: [],
      tableData2: [],
      editedData: {},
      editedTask: {},
      newUser: {
        name: '',
        gender: '',
        telephone: '',
      },
      newTask: {
        description: '',
        detail: '',
        type: '',
        price: '',
        publisher: '',
      },
      isVisible: false,
      isVisible2: false,
      dialogAddUserVisible: false,
      dialogAddTaskVisible: false,
      dialogEditUserVisible: false,
      dialogEditTaskVisible: false,
      formLabelWidth: '120px',
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    onSubmit() {
      console.log('submit!');
    },
    onClickUsers() {
      this.isVisible = true;
      this.isVisible2 = false;
    },
    onClickTasks() {
      this.isVisible2 = true;
      this.isVisible = false;
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
      this.tableData.splice(index, 1);
    },
    handleDelete1(index) {
      this.tableData2.splice(index, 1);
    },
    addUser() {
      this.tableData.push({...this.newUser});
      this.dialogAddUserVisible = false;
    },
    addTask() {
      this.tableData2.push({...this.newTask});
      this.dialogAddTaskVisible = false;
    },
    updateUser() {
      const index = this.tableData.findIndex(user => user.id === this.editedData.id);
      if (index !== -1) {
        this.tableData.splice(index, 1, this.editedData);
      }
      this.dialogEditUserVisible = false;
    },
    updateTask() {
      const index = this.tableData2.findIndex(task => task.id === this.editedTask.id);
      if (index !== -1) {
        this.tableData2.splice(index, 1, this.editedTask);
      }
      this.dialogEditTaskVisible = false;
    },
  },
};
</script>

<style scoped>
.el-dialog {
  width: 500px;
}
</style>
