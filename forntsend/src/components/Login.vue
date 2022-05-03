<!--
 * @Descripttion: 
 * @version: 1.0
 * @Author: suanzi
 * @Date: 2022-03-12 08:43:57
 * @LastEditors: suanzi
 * @LastEditTime: 2022-03-13 12:57:07
 * @FilePath: \forntsend\src\components\Login.vue
-->
<template>
  <div class="login_container">
    <div class="login_box">
      <div align="center" class="login_fornt">登录界面</div>
      <!-- 登录表单区域 -->
      <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="80px" class="login_form">
        <!-- 用户名 -->
        <el-form-item prop="username" label="用户名">
          <el-input v-model="loginForm.username" ></el-input>
        </el-form-item>
        <!-- 密码 -->
        <el-form-item prop="password" label="密码">
          <el-input v-model="loginForm.password"  type="password"></el-input>
        </el-form-item>
        <!-- 按钮区域 -->
        <el-form-item class="btns">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button type="info" @click="resetLoginForm">重置</el-button>
          <el-button type="info" @click="register">注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name:'Login',
   data() {
    return {
      // 这是登录表单的数据绑定对象
      loginForm: {
        username: '',
        password: ''
      },
      // 这是表单的验证规则对象
      loginFormRules: {
        // 验证用户名是否合法
        username: [
          { required: true, message: '请输入登录名称', trigger: 'blur' },
          { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' },
          { pattern:/^[A-Za-z0-9]+$/, message: '只能输入数字、字母', trigger: 'blur'}
        ],
        // 验证密码是否合法
        password: [
          { required: true, message: '请输入登录密码', trigger: 'blur' },
          { min: 3, max: 15, message: '长度在 3 到 15 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 点击重置按钮，重置登录表单
    resetLoginForm() {
      // console.log(this);
      this.$refs.loginFormRef.resetFields()
    },
    login() {
      this.$refs.loginFormRef.validate(async valid => {
        if (!valid) return
        this.$http.post('user',this.loginForm).then((result) => {
          console.log(result)
          if (result.data.status==1){
            window.sessionStorage.setItem('name',result.data.name)
            this.$message.success('登录成功')
            this.$router.push('/comment')
          }
          else if (result.data.status==0){
            this.$message.error('密码错误！')
          }
          else if (result.data.status==-1){
            this.$message.error('您还未注册！请先注册')
            this.$router.push('/register')
          }
        }).catch((err) => {
          console.error(err)
        })
      })
    },
    register(){
      this.$router.push('/register')
    }
  }
}
</script>

<style>
.login_container {
  background-color: #2b4b6b;
  height: 100%;
}

.login_box {
  width: 450px;
  height: 300px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
  /* transform: translate(20%); */
}

.btns {
  display: flex;
  justify-content: flex-end;
}
.login_fornt{
   width: 450px;
  height: 300px;
  position: absolute;
  transform: translate(0,50px);

}
</style>