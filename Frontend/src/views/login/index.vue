<template>
  <el-container class="cont-body">

    <el-header>
      <el-row :gutter="10">
        <el-col :xs="4" :md="1" class="cont-logo">
          <img :src="logTarifarito" alt="Tarifarito" class="imgLogtarifarito">
        </el-col>
        <el-col :xs="20" :md="23">
          <label class="text-logo">Tarifarito</label>
        </el-col>
      </el-row>
    </el-header>

    <el-main>
      <el-form ref="loginForm" label-position="top" :model="loginForm" :rules="loginRules" autocomplete="on">
        <div class="cont-card">
          <el-card class="box-card style-card" shadow="hover" :body-style="cardStyle">
            <div slot="header" class="clearfix" style="text-align: center;">
              <label style="font-size: x-large; color: white;">Iniciar sesión</label>
            </div>
            <el-row style="border: 1px solid #f5f5f5; padding: 3% 6% 6% 6%; border-radius: 5px;">
              <el-col :xs="24" :md="24">
                <el-form-item label="Usuario" prop="username">
                  <el-input
                    ref="username"
                    v-model="loginForm.username"
                    placeholder="Usuario"
                    name="username"
                    type="text"
                    tabindex="1"
                    autocomplete="on"
                    size="large"
                  />
                </el-form-item>
              </el-col>
              <el-col :xs="24" :md="24">
                <el-tooltip v-model="capsTooltip" content="Mayúscula" placement="right" manual>
                  <el-form-item label="Contraseña" prop="password">
                    <el-input
                      :key="passwordType"
                      ref="password"
                      v-model="loginForm.password"
                      :type="passwordType"
                      placeholder="Contraseña"
                      name="password"
                      tabindex="2"
                      autocomplete="on"
                      size="large"
                      @keyup.native="checkCapslock"
                      @blur="capsTooltip = false"
                      @keyup.enter.native="handleLogin"
                    />
                  </el-form-item>
                </el-tooltip>
              </el-col>
            </el-row>
            <el-row style="border: 0px solid; padding: 6% 6% 6% 6%;">
              <el-col style="border: 0px solid;" :xs="12" :md="10">
                <el-button :loading="loading" type="primary" style="width: 100%;" @click.native.prevent="handleLogin">Ingresar</el-button>
              </el-col>
              <el-col :xs="12" :md="14" style="padding-top: 0.6em; padding-left: 5%;">
                <a href="" style="color: #409EFF;">Crear cuenta</a>
              </el-col>
            </el-row>
          </el-card>
        </div>
      </el-form>
    </el-main>

    <div class="footer-login">
      <span class="textoFooter">
        SDEGC | CIAD - SUPERSERVICIOS ©&nbsp;2020
      </span>
    </div>
  </el-container>
</template>

<script>
import { validUsername } from '@/utils/validate'
import logSuper from '@/assets/superservicios1.png'
import logTarifarito from '@/assets/logo_buho.png'

export default {
  name: 'Login',
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Por favor ingrese un usuario válido'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(
          new Error('La contraseña no puede ser menor a seis caracteres')
        )
      } else {
        callback()
      }
    }
    return {
      logSuper: logSuper,
      logTarifarito: logTarifarito,
      loginForm: {
        username: '',
        password: ''
        // password: '111111'
      },
      loginRules: {
        username: [
          { required: true, trigger: 'blur', validator: validateUsername }
        ],
        password: [
          { required: true, trigger: 'blur', validator: validatePassword }
        ]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      redirect: undefined,
      otherQuery: {},
      cardStyle: {
        background: '#e9ecef'
      }
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        // const query = route.query // Captura la ruta anterior
        const query = { redirect: '/dashboard' }
        if (query) {
          this.redirect = query.redirect
          this.otherQuery = this.getOtherQuery(query)
        }
      },
      immediate: true
    }
  },
  created() {
    // window.addEventListener('storage', this.afterQRScan)
  },
  mounted() {
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    checkCapslock({ shiftKey, key } = {}) {
      if (key && key.length === 1) {
        if (
          (shiftKey && key >= 'a' && key <= 'z') ||
						(!shiftKey && key >= 'A' && key <= 'Z')
        ) {
          this.capsTooltip = true
        } else {
          this.capsTooltip = false
        }
      }
      if (key === 'CapsLock' && this.capsTooltip === true) {
        this.capsTooltip = false
      }
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          this.loading = true
          this.$store
            .dispatch('user/login', this.loginForm)
            .then(() => {
              this.$router.push({ path: this.redirect || '/' })
              this.loading = false
            })
            .catch(() => {
              this.loading = false
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    getOtherQuery(query) {
      return Object.keys(query).reduce((acc, cur) => {
        if (cur !== 'redirect') {
          acc[cur] = query[cur]
        }
        return acc
      }, {})
    }
  }
}
</script>

<style lang="scss">
	.el-header {
		background-color: #304156;
		line-height: 60px;
	}

  .imgLogtarifarito {
		height: 3em;
	}

	.cont-body {
		height: 100%;
	}

  .style-card {
    border: 1px solid #304156;
    background: #304156;
    border-radius: 10px;
    height: auto;
  }

  .footer-login {
		background-color: #304156;
		position: fixed;
		left: 0;
		bottom: 0;
		padding-bottom: 0.3%;
		width: 100%;
		color: white;
		text-align: center;
	}

  .textoFooter {
    vertical-align: middle;
    cursor: pointer;
    font-size: small;
    font-weight: bold;
  }

  // Pantallas superiores a 800px (PC)
	@media screen and (min-width: 800px) {
    .cont-logo {
      padding-top: 0.4%;
    }

    .text-logo {
      font-size: x-large;
      color: white;
    }

    .el-main {
      background-color: #e9eef3;
    }

    .cont-card {
      border: 0px solid green;
      padding: 4.5% 36% 0% 36%; // ARRIBA / DERECHA / ABAJO / IZQUIERDA
      height: 78vh;
      background: #f5f5f5;
      border-radius: 5px;
    }
	}

	// Pantallas inferiores a 800px (mobile)
	@media screen and (max-width: 800px) {
    .cont-logo {
      padding-top: 1%;
    }

    .text-logo {
      font-size: x-large;
      color: white;
    }

    .el-main {
      background-color: white;
    }

    .cont-card {
      border: 0px solid green;
      padding: 10% 0% 0% 0%;
    }
	}
</style>
