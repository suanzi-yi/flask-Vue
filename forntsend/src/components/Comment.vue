<!--
 * @Descripttion: 
 * @version: 1.0
 * @Author: suanzi
 * @Date: 2022-03-12 17:31:44
 * @LastEditors: suanzi
 * @LastEditTime: 2022-03-15 16:37:56
 * @FilePath: \forntsend\src\components\Comment.vue
-->
<template>
  <div>
    <el-card class="el-card-d" shadow="always">
      <div class="infinite-list-wrapper" style="overflow: auto">
        <el-timeline infinite-scroll-disabled="disabled" >
          <div v-if="isHas">
            <el-timeline-item
              v-for="item in comments"
              :key="item.id"
              :timestamp="item.time"
              placement="top"
              :color="color"
            >
              <el-card class="el-card-m" style="height: 120px">
                <el-button style="float: right; padding: 3px 0" icon="el-icon-delete" v-if="item.name==isMy()?true:false" @click="open(item.name,item.Id)"></el-button>
                <h4>{{ item.name }}：</h4>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ item.comments }}</p>
              </el-card>
            </el-timeline-item>
          </div>
          <div v-else>
            <el-timeline-item placement="top" :color="color">
              <el-card class="el-card-m" style="height: 120px">
                <h4>算子：</h4>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 说点什么吧😁</p>
              </el-card>
            </el-timeline-item>
          </div>
        </el-timeline>
      </div>
      <div class="el-card-messages">
        <el-input
          type="textarea"
          :rows="5"
          placeholder="输入留言"
          maxlength="200"
          v-model="message"
        ></el-input>
        <el-button
          type="info"
          round
          class="submit-message"
          @click="submitMessage"
          >留言</el-button
        >
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'Comment',
  data(){
      return {
          isHas:'',
          comments:[],
          message:'',
          color: '#0bbd87',
          isMy:function(){
           return window.sessionStorage.getItem("name")
          }
      }
  },
  created(){
      this.$http.get('comment').then((result) => {
           result= result.data
           console.log(result)
           if(result.status==0){
               this.isHas=false
           }
           else{
               this.isHas=true
               this.comments=result.comments
           }
      }).catch((err) => {
         console.log(err); 
      });
  },
  methods:{
      submitMessage(){
          var name=window.sessionStorage.getItem('name')
          var sub_mess={
              'name':name,
              'comment':this.message,
              'time':this.moment().format('YYYY-MM-DD hh:mm:ss')
          }
          console.log(sub_mess)
          if(sub_mess.comment){
             this.$http.post('insert',sub_mess).then((result) => {
              if(result.data.status==1){
                this.$message.success('留言成功！')
                this.isHas=true
                this.flush()
                this.message=''
                }
              else{
                  this.$message.error('留言失败！')
              }
          }).catch((err) => {
              console.log(err);
          })
          }
          else{
            this.$message.error('请不要提交空留言！')
          }
      },
      flush(){
          this.$http.get('comment').then((result) => {
           result= result.data
           console.log(result)
           this.comments=result.comments
        }).catch((err) => {
         console.log(err); 
        })
      },
      open(name,id) {
        this.$confirm('此操作将永久删除该评论, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          var delete_list={
            name: name,
            id: id
          }
          this.$http.post('delete', delete_list).then((result) => {
            if (result.data.status==1){
              this.$message({
              type: 'success',
              message: '删除成功!'
              })
              this.flush()
            }
            else{
              his.$message({
              type: 'error',
              message: '删除失败!'
              })
            }
          }).catch((err) => {
            console.error(err);
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })     
        })
      }
  }
}
</script>

<style scoped>
.infinite-list-wrapper {
  width: 100%;
  height: 500px;
}
.submit-message {
  width: 100%;
  background: rgb(235, 245, 247);
  color: cadetblue;
  letter-spacing: 20px;
}
@media screen and (max-width: 3000px) and (min-width: 767px) {
  .el-card-d {
    float: left;
    margin-top: 20px;
    margin-left: 10%;
    width: 80%;
    height: 90%;
  }
}
/*
  屏幕小于768px的
  */
@media screen and (max-width: 768px) and (min-width: 100px) {
  .el-card-d {
    width: 100%;
    height: 100%;
  }
}
</style>