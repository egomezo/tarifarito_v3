<template>
  <!-- <el-container class="cont-body"> -->
  <el-container v-show="!loginGestor" class="cont-body">
    <el-header>
      <el-row>
        <el-col :xs="6" :md="1" style="border: 0px solid red; text-align: center;">
          <img v-show="!x.matches" :src="logTarifarito" class="imgLogtarifarito" style="margin-top: 0.4em;">
          <img v-show="x.matches" :src="logTarifarito" class="imgLogtarifarito" style="margin-top: 1.4em;">
        </el-col>
        <el-col :xs="18" :md="16" style="border: 0px solid red;">
          <label v-show="!x.matches" style="font-size: x-large; color: white;">|&nbsp;&nbsp;&nbsp;Tarifarito</label>
          <label v-show="x.matches" style="font-size: 1em; color: white;">|&nbsp;&nbsp;&nbsp;Tarifarito</label>
        </el-col>
        <el-col :xs="0" :md="7" style="border: 0px solid red; text-align: right;">
          <img :src="logSuper" style="margin-top: 0.5%; height: 3.3em;">
        </el-col>
      </el-row>
    </el-header>

    <el-main>
      <el-form ref="loginForm" label-position="top" :model="loginForm" :rules="loginRules" autocomplete="on">
        <div class="cont-card">
          <el-card class="box-card style-card" shadow="hover" :body-style="cardStyle">
            <div slot="header" class="clearfix" style="text-align: center;">
              <label style="font-size: medium; color: white;">Iniciar sesión</label>
            </div>
            <el-row style="border: 1px solid #f5f5f5; padding: 3% 6% 6% 6%; border-radius: 5px;">
              <el-col :xs="24" :md="24">
                <el-form-item label="Correo" prop="username">
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
                      @keyup.enter.native="handleLoginBasic"
                    />
                  </el-form-item>
                </el-tooltip>
              </el-col>
            </el-row>
            <el-row style="border: 0px solid; padding: 6% 6% 6% 6%;">
              <el-col class="btn-login" :xs="24" :md="24">
                <el-button :loading="loading" type="primary" style="width: 100%;" @click.native.prevent="handleLoginBasic">Ingresar</el-button>
              </el-col>
              <!-- <el-col :xs="12" :md="14" style="padding-top: 0.6em; padding-left: 5%;">
                <a href="" style="color: #409EFF;">Recordar contraseña</a>
              </el-col> -->
            </el-row>
          </el-card>
        </div>
      </el-form>
    </el-main>

    <div class="footer-login">
      <span class="textoFooter">
        ::. . SUPERSERVICIOS - DTGE v2.2 ©&nbsp;2022 . .::
      </span>
    </div>
  </el-container>
</template>

<script>
import { validUserEmail } from '@/utils/validate'
import logSuper from '@/assets/super_dnp.jpg'
import logTarifarito from '@/assets/logo_buho.png'
import logoGov from '@/assets/logo_gov.svg'
import { getListNicknames, getListCorreos } from '@/api/tarifarito/usuarios'
// import md5 from 'md5'
import { mapGetters } from 'vuex'

export default {
  name: 'Login',
  data() {
    const validateUsername = (rule, value, callback) => {
      const usernameLower = value.toLowerCase()
      // console.log('usernameLower -> ', usernameLower)
      if (!validUserEmail(usernameLower)) {
        callback(new Error('Por favor ingrese un correo válido'))
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
      logTarifarito: logTarifarito,
      logSuper: logSuper,
      logoGov: logoGov,
      loginForm: {
        // username: '',
        // password: ''
        username: 'jherreraa@superservicios.gov.co',
        password: '123456'
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
      },
      listUsers: [],
      listCorreos: [],
      x: '',
      query: '',
      loginGestor: false
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'usuario', 'token'])
  },
  watch: {
    $route: {
      handler: function(route) {
        // console.log('Entro al observable del login!')
        // const query = route.query // Captura la ruta anterior
        // console.log('Ruta anterior --> ', query)
        // const query = { redirect: '/dashboard' }
        // if (query) {
        //   this.redirect = query.redirect
        //   this.otherQuery = this.getOtherQuery(query)
        // }
      },
      immediate: true
    }
  },
  created() {
    this.handleLogin()
    this.getNicknames()
    this.getCorreos()
    this.x = window.matchMedia('(max-width: 800px)')
  },
  mounted() {
    // console.log('Entro al login...')
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {},
  methods: {
    async getNicknames() {
      await getListNicknames().then((response) => {
        this.listUsers = response.users
        // console.log('NICkNAMES -> ', this.listUsers)
        const result = { data: response.nicknames }
        window.localStorage.setItem('usuarios', JSON.stringify(result))
      })
    },
    async getCorreos() {
      await getListCorreos().then((response) => {
        this.listCorreos = response.users
        // console.log('Correos -> ', this.listCorreos)
        const result = { data: response.correos }
        window.localStorage.setItem('correos', JSON.stringify(result))
      })
    },
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
      try { // Se valida si viene token de usuario desde el gestor
        // console.log('location :>> ', window.location)
        const valoresUrl = window.location.href.split('&')
        const urlParams = valoresUrl[1].split('gtjwt=')
        this.query = urlParams[1] // Se captura token de usuario (Si existe en la URL)
        // console.log('token :>> ', this.query)
        this.loginGestor = true
        this.handleLoginGestor()
      } catch (error) { // Si no viene token en la URL
        this.loginGestor = false
      }
      window.localStorage.setItem('login_gestor', this.loginGestor) // Se envia valor al localstorage
    },
    handleLoginBasic() {
      // this.loginForm.password = md5(this.loginForm.password)
      // console.log('contrasena -> ', this.loginForm.password)
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          this.loading = true
          const userInfo = { username: this.loginForm.username.trim(), password: btoa(this.loginForm.password), loginGestor: this.loginGestor, api: process.env.VUE_APP_GESTOR_API }
          this.$store
            .dispatch('user/login', userInfo)
            .then((data) => {
              // console.log('store login --> ', data)
              const userLogged = this.listCorreos.find(user => user.correo === this.loginForm.username.toLowerCase()).nombre
              this.$notify({
                title: `Hola ${userLogged}`,
                message: `Se ha iniciado tu sesión exitosamente!`,
                position: 'bottom-right',
                type: 'success'
              })
              this.$router.push({ path: this.redirect || '/' })
              this.loading = false
              // this.loginForm.password = ''
            })
            .catch((err) => {
              console.log('error login -> ', err)
              this.$notify.error({
                title: 'Error',
                message: 'Contraseña incorrecta'
              })
              this.loading = false
              this.loginForm.password = ''
            })
        } else {
          console.log('error submit!!')
          this.loginForm.password = ''
          return false
        }
      })
    },
    handleLoginGestor() {
      const userInfo = { token: this.query, loginGestor: this.loginGestor }
      this.$store
        .dispatch('user/login', userInfo)
        .then((data) => {
          this.$notify({
            title: `Hola`,
            message: `Se ha iniciado tu sesión exitosamente!`,
            position: 'bottom-right',
            type: 'success'
          })
          this.$router.push({ path: this.redirect || '/' })
        })
        .catch((err) => {
          console.log('error login -> ', err)
          this.$notify.error({
            title: 'Error',
            message: 'Error en sesión de usuario'
          })
          // window.location.replace('http://localhost:4200')
          // window.location.replace(process.env.VUE_APP_GESTOR_FRONT)
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

    .btn-login {
      border: 0px solid;
      // padding-left: 20%;
      // padding-right: 20%;
    }
	}

	// Pantallas inferiores a 800px (mobile)
	@media screen and (max-width: 800px) {
    .el-main {
      background-color: white;
    }

    .cont-card {
      border: 0px solid green;
      padding: 10% 0% 0% 0%;
    }
	}
</style>
