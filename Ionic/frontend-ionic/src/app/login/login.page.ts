import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage {
  username: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private http: HttpClient, private router: Router) {}

  login() {
    const loginData = {
      username: this.username,
      password: this.password,
    };

    // Substitua pela URL do endpoint do Django
    this.http.post('http://127.0.0.1:8000/api/token/', loginData).subscribe({
      next: (response: any) => {
        // Salvar o token no localStorage ou sessionStorage
        localStorage.setItem('access', response.access);
        localStorage.setItem('refresh', response.refresh);

        // Redirecionar para a página principal
        this.router.navigate(['/home']);
      },
      error: (error) => {
        this.errorMessage = 'Credenciais inválidas. Tente novamente.';
        console.error('Erro no login:', error);
      },
    });
  }
}
