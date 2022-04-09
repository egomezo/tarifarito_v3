<template>
  <div class="app-container" style="text-align: center;">
    <upload-excel-component
      :on-success="handleSuccess"
      :before-upload="beforeUpload"
    />
    <div v-if="tableData.length" style="padding-top: 2%;">
      <el-button
        :loading="loading"
        style="border: 1px solid #67c23a;"
        size="medium"
        icon="el-icon-upload"
        round
        @click="clickCargar();"
      >Cargar {{ tableData.length }} expedientes</el-button>
      <div style="padding-top: 2%;">
        <el-progress :text-inside="true" :stroke-width="24" :percentage="uploadProgress" :color="customColorMethod" status="success" />
      </div>
    </div>
    <el-table
      :data="tableData"
      border
      highlight-current-row
      style="width: 100%; margin-top: 20px"
    >
      <el-table-column
        v-for="item of tableHeader"
        :key="item"
        :prop="item"
        :label="item"
        align="center"
      />
      <el-table-column align="center">
        <template slot-scope="scope">
          <el-button
            type="text"
            size="small"
            @click="deleteRow(scope.$index, tableData)"
          >
            Eliminar
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import UploadExcelComponent from '@/components/UploadExcel/index.vue'
import { createProceso } from '@/api/procesosDIEG/procesos'
import moment from 'moment'
export default {
  name: 'UploadExcel',
  components: { UploadExcelComponent },
  data() {
    return {
      tableData: [],
      tableHeader: [],
      uploadProgress: 0,
      loading: false
    }
  },
  methods: {
    beforeUpload(file) {
      const isLt1M = file.size / 1024 / 1024 < 1
      if (isLt1M) {
        return true
      }
      this.$message({
        message: 'Please do not upload files larger than 1m in size.',
        type: 'warning'
      })
      return false
    },
    handleSuccess({ results, header }) {
      this.tableData = results
      this.tableHeader = header
    },
    deleteRow(index, rows) {
      rows.splice(index, 1)
    },
    async clickCargar() {
      this.loading = true
      const procesosLength = this.tableData.length
      let countProgress = 0
      let procesosCargados = 0
      let procesosError = 0
      while (this.tableData.length) {
        const element = this.tableData[0]
        if (!isNaN(element.fecha_caducidad_sancion)) { // Si es un numero
          element.fecha_caducidad_sancion = moment(this.numeroAFecha(element.fecha_caducidad_sancion, true)).format('DD/MM/YYYY')
        }
        await createProceso(element).then((response) => {
          procesosCargados += 1
          this.deleteRow(0, this.tableData)
          countProgress = countProgress + 100
          this.uploadProgress = parseInt(countProgress / procesosLength)
        }, (err) => {
          console.log(err)
          procesosError += 1
          this.deleteRow(0, this.tableData)
          countProgress = countProgress + 100
          this.uploadProgress = parseInt(countProgress / procesosLength)
        })
      }
      if (procesosCargados > 0) {
        this.$notify({
          title: 'Buen trabajo!',
          message: `Expedientes cargados con éxito: ${procesosCargados} `,
          type: 'success',
          duration: 3000,
          showClose: false
        })
      }
      if (procesosError > 0) {
        this.$notify({
          title: 'Error',
          message: `Expedientes con error en la carga: ${procesosError}`,
          type: 'error',
          duration: 3000,
          position: 'bottom-right',
          showClose: false
        })
      }
      this.uploadProgress = 0
      this.tableHeader = []
      this.loading = false
    },
    numeroAFecha(numeroDeDias, esExcel = false) {
      var diasDesde1900 = esExcel ? 25567 + 1 : 25567
      // 86400 es el número de segundos en un día, luego multiplicamos por 1000 para obtener milisegundos.
      return new Date((numeroDeDias - diasDesde1900) * 86400 * 1000)
    },
    customColorMethod(percentage) {
      if (percentage < 30) {
        return '#f56c6c'
      } else if (percentage < 70) {
        return '#e6a23c'
      } else {
        return '#67c23a'
      }
    }
  }
}
</script>
