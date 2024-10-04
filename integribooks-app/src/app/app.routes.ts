import { Routes } from '@angular/router';
import { AdminComponent } from './admin/admin.component';
import { HomeComponent } from './home/home.component';
import { MainLayoutComponent } from './layout/main-layout/main-layout.component';
import { LibraryComponent } from './library/library.component';

export const routes: Routes = [
  {
    path: '',
    component: MainLayoutComponent,
    children: [
      { path: '', component: HomeComponent },
      { path: 'library', component: LibraryComponent },
      { path: 'admin', component: AdminComponent },
      { path: '**', redirectTo: '', pathMatch: 'full' },
    ],
  },
];
