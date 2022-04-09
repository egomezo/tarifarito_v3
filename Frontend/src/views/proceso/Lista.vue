<template>
  <div class="createPost-container" style="background: #f7fbff; height: 87vh;">
    <sticky class-name="sub-navbar">
      <div style="border: 0px solid red; text-align: center">
        <!-- Boton para agregar nuevo expediente al aplicativo -->
        <div v-show="showOnlyAdmin">
          <transition name="el-zoom-in-bottom">
            <div v-show="!loading" class="transition-box">
              <el-button
                style="border: 1px solid #67c23a"
                size="medium"
                icon="el-icon-circle-plus"
                round
                @click="
                  clickAgregar();
                  msgAgregarVisible = true;
                "
              >Agregar expediente</el-button>
            </div>
          </transition>
        </div>

        <div v-show="!showOnlyAdmin" style="text-align: center; color: white">
          <label style="font-size: x-large">{{ usuario }}</label>
        </div>
      </div>
    </sticky>

    <!-- Cuadro de dialogo para agregar expediente -->

    <el-dialog
      v-el-drag-dialog
      :visible.sync="msgAgregarVisible"
      :before-close="closeModalAgregar"
      width="36em"
      custom-class="dialog-class-lista"
      :show-close="false"
    >
      <sticky class-name="sub-navbar">
        <div style="border: 0px solid red; color: white; text-align: center">
          <h2>Agregar expediente</h2>
        </div>
      </sticky>
      <div
        class="createPost-container"
        style="padding-top: 35px; padding-bottom: 20px; padding-left: 13px"
      >
        <el-form
          ref="formAgregar"
          :model="formAgregar"
          :rules="rulesFormProceso"
          label-width="145px"
          class="demo-ruleForm"
        >
          <el-form-item label="Expediente" prop="radicado">
            <el-input
              v-model="formAgregar.radicado"
              autocomplete="off"
              placeholder="Ingrese No. del expediente"
              maxlength="17"
              show-word-limit
              clearable
              class="control-modal"
            />
          </el-form-item>
          <el-form-item label="Servicio" prop="servicio">
            <el-select
              v-model="formAgregar.servicio"
              filterable
              placeholder="Seleccione el servicio"
              class="control-modal"
              clearable
              @change="selectServicio($event)"
              @clear="clearSelect()"
            >
              <el-option
                v-for="item in datosServicios"
                :key="item.idservicio"
                :label="item.servicio"
                :value="item.idservicio"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="Empresa" prop="empresa">
            <el-select
              v-model="formAgregar.empresa"
              filterable
              :disabled="disableEmpresas"
              placeholder="Seleccione un prestador"
              class="control-modal"
              clearable
            >
              <el-option
                v-for="item in datosEmpresas"
                :key="item.id_empresa"
                :label="item.nombre"
                :value="item.id_empresa"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="Proyectista" prop="usuario">
            <el-select
              v-model="formAgregar.usuario"
              filterable
              placeholder="Seleccione un abogado"
              class="control-modal"
              clearable
            >
              <el-option
                v-for="item in datosUsuarios"
                :key="item.idusuario"
                :label="item.nombre + ' ' + item.apellido"
                :value="item.idusuario"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="Revisor" prop="revisor">
            <el-select
              v-model="formAgregar.revisor"
              filterable
              placeholder="Seleccione un revisor"
              class="control-modal"
              clearable
            >
              <el-option
                v-for="item in datosRevisor"
                :key="item.idusuario"
                :label="item.nombre + ' ' + item.apellido"
                :value="item.idusuario"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="Caducidad sanción" prop="fecha_caducidad_sancion" clearable>
            <el-date-picker
              v-model="formAgregar.fecha_caducidad_sancion"
              type="date"
              placeholder="Seleccione la fecha"
              class="control-modal"
            />
          </el-form-item>
          <el-form-item label="Caducidad recurso" prop="fecha_caducidad_recurso" clearable>
            <el-date-picker
              v-model="formAgregar.fecha_caducidad_recurso"
              type="date"
              placeholder="Seleccione la fecha"
              class="control-modal"
            />
          </el-form-item>
          <el-form-item>
            <el-button
              @click="
                resetForm('formAgregar');
                msgAgregarVisible = false;
              "
            >Cancelar</el-button>
            <el-button
              type="success"
              @click="agregarExpediente('formAgregar')"
            >Agregar</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-dialog>

    <!-- Cuadro de dialogo para asignar abogado -->

    <el-dialog
      v-el-drag-dialog
      :visible.sync="msgUsuarioVisible"
      width="35em"
      custom-class="dialog-class-lista"
      center
      :show-close="false"
    >
      <sticky class-name="sub-navbar">
        <div style="border: 0px solid red; color: white; text-align: center">
          <h2>Modificar asignación de usuarios</h2>
        </div>
      </sticky>
      <div
        class="createPost-container"
        style="padding-top: 35px; padding-bottom: 5px; padding-left: 20px"
      >
        <el-form :model="formUsuario" label-width="120px" class="demo-ruleForm">
          <el-form-item label="Expediente">
            <el-input
              v-model="formUsuario.expediente"
              autocomplete="off"
              placeholder="Ingrese No. del expediente"
              maxlength="14"
              show-word-limit
              clearable
              class="control-modal"
              readonly
            />
          </el-form-item>
          <el-form-item label="Proyectista">
            <el-select
              v-model="formUsuario.usuario"
              filterable
              placeholder="Seleccione un abogado"
              class="control-modal"
            >
              <el-option
                v-for="item in datosUsuarios"
                :key="item.idusuario"
                :label="item.nombre + ' ' + item.apellido"
                :value="item.idusuario"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="Revisor">
            <el-select
              v-model="formUsuario.revisor"
              filterable
              placeholder="Seleccione un revisor"
              class="control-modal"
            >
              <el-option
                v-for="item in datosRevisor"
                :key="item.idusuario"
                :label="item.nombre + ' ' + item.apellido"
                :value="item.idusuario"
              />
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button @click="msgUsuarioVisible = false">Cancelar</el-button>
            <el-button
              type="success"
              @click="
                msgUsuarioVisible = false;
                asignarUsuario();
              "
            >Asignar</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-dialog>

    <!-- Dialogo que se aparece cuando se va a eliminar un expediente -->

    <el-dialog
      v-el-drag-dialog
      title="Advertencia"
      :visible.sync="deleteDialogVisible"
      width="35%"
      center
      custom-class="dialog-class-lista"
      :show-close="false"
    >
      <br>
      <center>
        <span>¿Realmente desea eliminar el expediente <b>No. {{ delExpediente }}</b>?</span>
      </center>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deleteDialogVisible = false">Cancelar</el-button>
        <el-button
          type="primary"
          @click="borrarExpediente"
        >Confirmar</el-button>
      </span>
    </el-dialog>

    <!-- Tabla donde se lista, ordena y realiza busqueda de los expedientes -->

    <div class="app-container">
      <el-card class="box-card">
        <!-- <el-input v-model="filename" placeholder="Nombre de archivo (defecto lista-excel)" size="mini" style="width:300px;" prefix-icon="el-icon-document" /> -->
        <el-button :loading="downloadLoading" round style="margin-bottom:20px; border: 1px solid #67C23A;" size="mini" type="success" plain icon="el-icon-download" @click="handleDownload">
          <span><b>Exportar a Excel los procesos seleccionados</b></span>
        </el-button>
        <el-table
          ref="multipleTable"
          v-loading="loading"
          style="width: 100%; border: 1px solid #d8ebff;"
          height="65vh"
          element-loading-text=""
          border
          fit
          highlight-current-row
          :data="datosProcesos"
          @selection-change="handleSelectionChange"
        >
          <el-table-column type="selection" align="center" />
          <el-table-column
            v-for="column in tableColumns"
            :key="column.label"
            :label="column.label"
            :prop="column.prop"
            align="center"
            :width="column.width"
            sortable
            :filters="getFilters(column.filter)"
            :filter-method="filterHandler"
          >
            <template slot-scope="scope">
              <div v-if="column.prop === 'empresa'" class="keepAll">{{ scope.row[column.prop] }}</div>
              <div v-else-if="column.prop === 'estado'" class="keepAll">{{ scope.row[column.prop] }}</div>
              <div v-else-if="column.prop === 'usuario'"><el-tag type="primary">{{ scope.row[column.prop] }}</el-tag></div>
              <div v-else-if="column.prop === 'revisor'"><el-tag type="info">{{ scope.row[column.prop] }}</el-tag></div>
              <div v-else-if="column.prop === 'caducidadsancion'"><i class="el-icon-time" /> {{ convertDate(scope.row[column.prop]) }}</div>
              <div v-else>{{ scope.row[column.prop] }}</div>
            </template>
          </el-table-column>
          <el-table-column align="center" :width="showOnlyAdmin ? 190 : 190">
            <!-- eslint-disable-next-line -->
            <template slot="header" slot-scope="scope">
              <el-input
                v-model="busquedaExpediente"
                size="mini"
                placeholder="No. Expediente"
                clearable
                @input="buscarProcesos"
              />
            </template>
            <template slot-scope="scope">
              <el-button
                v-show="showOnlyAdmin"
                style="border: 1px solid #409eff;"
                size="mini"
                icon="el-icon-user-solid"
                @click="handlePermisos(scope.row)"
              />
              <el-button
                size="mini"
                type="success"
                @click="handleProceso(scope.row)"
              ><b>Ver</b></el-button>
              <el-button
                v-show="showOnlyAdmin"
                size="mini"
                type="danger"
                icon="el-icon-delete-solid"
                @click="handleDelete(scope.row)"
              />
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { CONSTANTS } from '@/constants/constants'
import { getListProcesos, createProceso, updateProcesoUsuario, deleteProceso } from '@/api/procesosDIEG/procesos'
import { getListUsuarios, getListRevisores } from '@/api/procesosDIEG/usuarios'
import { getListServicios } from '@/api/procesosDIEG/servicios'
import { getListEmpresas } from '@/api/procesosDIEG/empresas'
import { getAllEmpresas } from '@/api/procesosDIEG/empresas'
// import { getRoles } from '@/api/role'
// import { addRole } from '@/api/role'
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import Sticky from '@/components/Sticky' // 粘性header组件
import moment from 'moment'

export default {
  name: 'ViewProcesos',
  directives: { elDragDialog },
  components: { Sticky },
  data() {
    return {
      dialogTableVisible: false,
      /* Datos para mostrar en la tabla */
      tableColumns: [],
      filters: {},
      filterExpediente: [],
      filterEmpresa: [],
      filterServicio: [],
      filterEstado: [],
      filterCaducidadsancion: [],
      filterAbogado: [],
      filterRevisor: [],
      datosProcesos: [],
      datosUsuarios: [],
      datosRevisor: [],
      datosServicios: [],
      datosEmpresas: [],
      allDataEmpresas: [],
      /* Datos para captar la creación */
      formAgregar: CONSTANTS.formAgregar,
      rulesFormProceso: CONSTANTS.rulesFormProceso,
      formUsuario: CONSTANTS.formUsuario,
      /* Aqui se guarda el valor escrito en el cuadro de texto para la busqueda */
      busquedaExpediente: '',
      /* Si es o no visible el fomulario de agregar */
      msgAgregarVisible: false,
      /* Si es o no visible el formulario de asginación de usuario */
      msgUsuarioVisible: false,
      /* Si es o no visible el cuadro de confirmación de eliminación */
      deleteDialogVisible: false,
      delExpediente: '',
      delIdproceso: '',
      loading: true,
      disableEmpresas: true,
      showOnlyAdmin: false,
      multipleSelection: [],
      downloadLoading: false,
      filename: ''
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'usuario', 'idusuario', 'dependencia'])
  },
  created() {
    this.initView()
  },
  methods: {
    convertDate(val) {
      // console.log('convertDate -> ', val)
      if (val !== 'No registra') {
        return moment(val).format('DD/MM/YYYY')
      } else {
        return 'No registra'
      }
    },
    buscarProcesos() {
      const procesos = JSON.parse(window.localStorage.getItem('procesos'))
      this.datosProcesos = procesos.filter((data) => !this.busquedaExpediente || data.expediente.toLowerCase().includes(this.busquedaExpediente.toLowerCase()))
    },
    handleSelectionChange(val) {
      // console.log(val)
      this.multipleSelection = val
    },
    handleDownload() {
      if (this.multipleSelection.length) {
        this.downloadLoading = true
        import('@/vendor/Export2Excel').then(excel => {
          const tHeader = ['EXPEDIENTE', 'SERVICIO', 'EMPRESA', 'CADUCIDAD O FECHA VENCIMIENTO/ TÉRMINO PARA RESOLVER REP(DD-MM-AA)', 'ESTADO', 'PROYECTISTA', 'REVISOR']
          const filterVal = ['expediente', 'servicio', 'empresa', 'caducidadsancion', 'estado', 'usuario', 'revisor']
          const list = this.multipleSelection
          const data = this.formatJson(filterVal, list)
          excel.export_json_to_excel({
            header: tHeader,
            data,
            filename: this.filename
          })
          this.$refs.multipleTable.clearSelection()
          this.downloadLoading = false
        })
      } else {
        this.$message({
          message: 'Seleccione al menos un proceso',
          type: 'warning'
        })
      }
    },
    formatJson(filterVal, jsonData) {
      return jsonData.map(v => filterVal.map(j => v[j]))
    },
    initView() {
      if (this.roles[0] === 'administrador') {
        this.showOnlyAdmin = true
        this.tableColumns = CONSTANTS.tableColumnsAdmin
      } else {
        this.tableColumns = CONSTANTS.tableColumnsAbogado
      }
      this.getProcesos()
      this.getUsuarios()
      this.getRevisores()
      this.getServicios()
      this.getEmpresas()
    },
    async getProcesos() {
      await getListProcesos(this.dependencia).then((response) => {
        // console.log('Lista de proecesos -> ', response)
        let procesos = []
        if (this.roles[0] === 'administrador') {
          procesos = response
        } else if (this.roles[0] === 'revisor') {
          procesos = response.filter((proceso) => proceso.idrevisor === this.idusuario)
        } else {
          procesos = response.filter((proceso) => proceso.idusuario === this.idusuario)
        }
        procesos = procesos.map((proceso) => {
          if (proceso.caducidadsancion !== 'None') {
            const mes = moment(proceso.caducidadsancion).format('MM')
            const ano = moment(proceso.caducidadsancion).format('YYYY')
            proceso.textCaducidadsancion = ano + '-' + mes
            proceso.valueCaducidadsancion = mes + '/' + ano
            proceso.caducidadsancion = new Date(moment(proceso.caducidadsancion).format('YYYY/MM/DD HH:mm:ss')) // Se transforma la caducidadsancion a tipo fecha
          } else {
            proceso.textCaducidadsancion = 'No registra'
            proceso.valueCaducidadsancion = 'No registra'
            proceso.caducidadsancion = 'No registra'
          }
          // console.log(proceso.caducidadsancion)
          return proceso
        })
        window.localStorage.setItem('procesos', JSON.stringify(procesos))
        this.datosProcesos = procesos
        this.loading = false
        // console.log('Procesos -> ', this.datosProcesos)
        this.setFilters()
      })
    },
    setFilters() {
      this.datosProcesos.forEach((item) => {
        // console.log(item)
        this.filterExpediente.push({ text: item.expediente, value: item.expediente })
        this.filterEmpresa.push({ text: item.empresa, value: item.empresa })
        this.filterServicio.push({ text: item.servicio, value: item.servicio })
        this.filterEstado.push({ text: item.estado, value: item.estado })
        this.filterCaducidadsancion.push({ text: item.textCaducidadsancion, value: item.valueCaducidadsancion })
        this.filterAbogado.push({ text: item.usuario, value: item.usuario })
        this.filterRevisor.push({ text: item.revisor, value: item.revisor })
      })
      this.filters.filterExpediente = this.getUniqueListBy(this.filterExpediente, 'text')
      this.filters.filterEmpresa = this.getUniqueListBy(this.filterEmpresa, 'text')
      this.filters.filterServicio = this.getUniqueListBy(this.filterServicio, 'text')
      this.filters.filterEstado = this.getUniqueListBy(this.filterEstado, 'text')
      this.filters.filterCaducidadsancion = this.getUniqueListBy(this.filterCaducidadsancion, 'text')
      this.filters.filterCaducidadsancion = this.orderByDate(this.filters.filterCaducidadsancion)
      this.filters.filterAbogado = this.getUniqueListBy(this.filterAbogado, 'text')
      this.filters.filterRevisor = this.getUniqueListBy(this.filterRevisor, 'text')
    },
    getUniqueListBy(arr, key) {
      return [...new Map(arr.map(item => [item[key], item])).values()]
    },
    getFilters(val) {
      // console.log(this.filters[val])
      return this.filters[val]
    },
    orderByDate(arr) {
      arr.forEach((item, index) => {
        if (item.text === 'No registra') {
          arr.splice(index, 1)
        }
      })
      const newArr = [...arr.sort((a, b) => {
        // console.log(a.text.substring(0, 4), '-', b.text.substring(0, 4))
        return b.text.substring(0, 4) - a.text.substring(0, 4)
      })]
      newArr.unshift({ text: 'No registra', value: 'No registra' })
      return newArr
    },
    async getUsuarios() {
      await getListUsuarios(this.dependencia).then((response) => {
        // console.log('Usuarios -> ', response)
        this.datosUsuarios = response
      })
    },
    async getRevisores() {
      await getListRevisores(this.dependencia).then((response) => {
        // console.log('Revisores -> ', response)
        this.datosRevisor = response
      })
    },
    async getServicios() {
      await getListServicios(this.dependencia).then((response) => {
        this.datosServicios = response
      })
    },
    async getEmpresas() {
      await getAllEmpresas().then((response) => {
        this.allDataEmpresas = response.items
        window.localStorage.setItem(
          'empresas',
          JSON.stringify(this.allDataEmpresas)
        )
        // console.log(this.allDataEmpresas.items)
      })
    },
    /* Metodo para realizar la busqueda de los filtros ubicado en las columnas */
    filterHandler(value, row, column) {
      const property = column['property']
      let valueProperty = row[property]
      if (property === 'caducidadsancion') {
        if (valueProperty !== 'No registra') {
          valueProperty = moment(valueProperty).format('DD/MM/YYYY').substring(3, 10)
        }
      }
      // console.log('value -> ', value, ' row -> ', valueProperty, ' column -> ', property)
      return valueProperty === value
    },
    /* Evento click boton permisos */
    handlePermisos(data) {
      this.formUsuario.idproceso = data.idproceso
      this.formUsuario.expediente = data.expediente
      this.formUsuario.usuario = data.idusuario
      this.formUsuario.revisor = data.idrevisor
      this.msgUsuarioVisible = true
    },
    /* Evento clic boton permisos */
    handleDelete(data) {
      this.delIdproceso = data.idproceso
      this.delExpediente = data.expediente
      this.deleteDialogVisible = true
    },
    async borrarExpediente() {
      this.loading = true
      await deleteProceso(this.delIdproceso).then((response) => {
        this.$notify({
          title: 'Información',
          message: 'Se ha eliminado el expediente',
          type: 'warning',
          duration: 2000
        })
        this.getProcesos()
      })
      this.deleteDialogVisible = false
    },
    async asignarUsuario() {
      this.loading = true
      await updateProcesoUsuario(this.formUsuario).then((response) => {
        this.$notify({
          title: 'Bien hecho!',
          message: 'Expediente actualizado con éxito',
          type: 'success',
          duration: 2000
        })
        this.getProcesos()
      })
    },
    async selectServicio(idservicio) {
      if (this.formAgregar.empresa) {
        this.disableEmpresas = true
        delete this.formAgregar.empresa
      }
      if (idservicio) {
        await getListEmpresas(idservicio).then((response) => {
          this.datosEmpresas = response.items
          this.disableEmpresas = false
        })
      }
    },
    clickAgregar() {
      this.formAgregar = {}
      this.disableEmpresas = true
    },
    async agregarExpediente(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.msgAgregarVisible = false
          // console.log(this.formAgregar)
          this.loading = true
          this.formAgregar.dependencia = this.dependencia
          // console.log('FORMAGREGAR -> ', this.formAgregar)
          createProceso(this.formAgregar).then((response) => {
            this.$notify({
              title: 'Buen trabajo!',
              message: 'Expediente agregado con éxito',
              type: 'success',
              duration: 2000
            })
            this.getProcesos()
            this.$refs['formAgregar'].resetFields()
          }, (err) => {
            console.log(err)
            this.$notify({
              title: 'Error',
              message: 'Número de expediente ya existe',
              type: 'error',
              duration: 2000
            })
            this.getProcesos()
            this.$refs['formAgregar'].resetFields()
          })
        } else {
          // console.log('error submit!!')
          return false
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    clearSelect() {
      this.formAgregar.empresa = ''
      this.disableEmpresas = true
    },
    closeModalAgregar() {
      this.$refs['formAgregar'].resetFields()
      this.msgAgregarVisible = false
    },
    handleProceso(proceso) {
      // console.log(`/procesos/detalle/${proceso.idproceso}/${JSON.stringify(proceso)}/${JSON.stringify(this.datosUsuarios)}/${JSON.stringify(this.datosServicios)}`)
      this.$router.push({
        path: `/procesos/detalle/${proceso.idproceso}`
      })
      // this.$router.push({
      //   path: `/procesos/detalle/${proceso.idproceso}/${JSON.stringify(
      //     this.datosServicios
      //   )}/${JSON.stringify(this.datosUsuarios)}`
      // })
      // this.$router.push({ path: `/procesos/detalle/${idproceso}/${JSON.stringify(this.datosUsuarios)}/${JSON.stringify(this.datosServicios)}/${JSON.stringify(this.allDataEmpresas)}` })
      // this.$router.push(
      //   {
      //     name: 'DetalleProceso',
      //     params: {
      //       id: idproceso,
      //       usuarios: this.datosUsuarios,
      //       servicios: this.datosServicios,
      //       empresas: this.allDataEmpresas
      //     }
      //   }
      // )
    }
  }
}
</script>

<style lang="scss" scoped>
.keepAll {
  word-break: keep-all;
}
.control-modal {
  width: 25em;
}
</style>

<style lang="scss">
.dialog-class-lista {
  border-radius: 10px;
}

.dialog-class-lista .el-dialog__body {
  padding-top: 0 !important;
}

.dialog-class-agregar .el-dialog__header {
  border: 1px solid red;
  border-radius: 10px;
  display: none;
}

.dialog-class-agregar .el-dialog__body {
  margin: 0 !important;
  padding: 0 !important;
}
</style>
